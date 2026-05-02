import psycopg2

# DEFENSE: We use psycopg2 to connect Python to the PostgreSQL database.
# Change password='123' to your actual PostgreSQL password!
DB_CONFIG = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "kasym147208a11..", 
    "host": "localhost",
    "client_encoding": "utf8"
}

def get_connection():
    # EXPLANATION: Establishes a connection to the database using the config dictionary.
    return psycopg2.connect(**DB_CONFIG)

def init_db():
    """Creates tables if they don't exist yet."""
    conn = get_connection()
    cur = conn.cursor()
    
    # DEFENSE: Using standard SQL to create tables. 'SERIAL' auto-increments the ID.
    cur.execute('''
        CREATE TABLE IF NOT EXISTS players (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL
        )
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS game_sessions (
            id SERIAL PRIMARY KEY,
            player_id INTEGER REFERENCES players(id),
            score INTEGER NOT NULL,
            level_reached INTEGER NOT NULL,
            played_at TIMESTAMP DEFAULT NOW()
        )
    ''')
    conn.commit()
    cur.close()
    conn.close()

def save_score(username, score, level):
    # EXPLANATION: Saves the final score. If the user doesn't exist, it adds them first.
    conn = get_connection()
    cur = conn.cursor()
    
    # 1. Insert user if they don't exist, and get their ID
    cur.execute('''
        INSERT INTO players (username) VALUES (%s)
        ON CONFLICT (username) DO NOTHING;
    ''', (username,))
    
    cur.execute('SELECT id FROM players WHERE username = %s', (username,))
    player_id = cur.fetchone()[0]
    
    # 2. Insert the game session
    cur.execute('''
        INSERT INTO game_sessions (player_id, score, level_reached) 
        VALUES (%s, %s, %s)
    ''', (player_id, score, level))
    
    conn.commit()
    cur.close()
    conn.close()

def get_top_10():
    # DEFENSE: Uses 'ORDER BY score DESC' to sort from highest to lowest score.
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''
        SELECT p.username, g.score, g.level_reached 
        FROM game_sessions g
        JOIN players p ON g.player_id = p.id
        ORDER BY g.score DESC
        LIMIT 10
    ''')
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results

def get_personal_best(username):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''
        SELECT MAX(g.score) 
        FROM game_sessions g
        JOIN players p ON g.player_id = p.id
        WHERE p.username = %s
    ''', (username,))
    result = cur.fetchone()[0]
    cur.close()
    conn.close()
    return result if result is not None else 0