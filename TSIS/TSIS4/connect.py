import psycopg2
from config import load_config

# DEFENSE: This function creates and returns a database connection using psycopg2.
# We call this whenever we need to talk to PostgreSQL.
def get_connection():
    try:
        params = load_config()
        conn = psycopg2.connect(**params)
        return conn
    except Exception as error:
        print(f"Error connecting to DB: {error}")
        return None