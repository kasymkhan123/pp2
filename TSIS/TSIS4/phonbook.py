import psycopg2
import json
import csv
from connect import get_connection

def run_sql_file(filename):
    """DEFENSE: Reads a .sql file and executes it. Used for easy setup."""
    conn = get_connection()
    if conn is None: return
    try:
        with open(filename, 'r') as file:
            sql = file.read()
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()
        print(f"Successfully executed {filename}")
    except Exception as e:
        print(f"Error executing {filename}: {e}")
    finally:
        conn.close()

def view_contacts_paginated():
    """DEFENSE: Implements pagination using LIMIT and OFFSET, plus dynamic ORDER BY."""
    conn = get_connection()
    if not conn: return
    cur = conn.cursor()

    print("\n--- Sort & Filter ---")
    sort_choice = input("Sort by (1: Name, 2: Birthday, 3: Date Added): ")
    group_filter = input("Filter by group name (leave blank for all): ")

    order_by = "c.name"
    if sort_choice == '2': order_by = "c.birthday"
    elif sort_choice == '3': order_by = "c.created_at"

    limit = 3
    offset = 0

    while True:
        # DEFENSE: Building the query dynamically based on user filter.
        query = f"""
            SELECT c.name, c.email, c.birthday, g.name 
            FROM contacts c 
            LEFT JOIN groups g ON c.group_id = g.id
        """
        params = []
        if group_filter:
            query += " WHERE g.name ILIKE %s"
            params.append(f"%{group_filter}%")
        
        query += f" ORDER BY {order_by} LIMIT %s OFFSET %s"
        params.extend([limit, offset])

        cur.execute(query, tuple(params))
        rows = cur.fetchall()

        print(f"\n--- Page {offset//limit + 1} ---")
        if not rows:
            print("No contacts found on this page.")
        else:
            for row in rows:
                print(f"Name: {row[0]}, Email: {row[1]}, BDay: {row[2]}, Group: {row[3]}")

        action = input("\n[N]ext page, [P]rev page, [Q]uit: ").lower()
        if action == 'n':
            offset += limit
        elif action == 'p':
            offset = max(0, offset - limit) # DEFENSE: max(0) prevents negative offsets
        elif action == 'q':
            break

    cur.close()
    conn.close()

def search_contacts():
    """DEFENSE: Calls the PL/pgSQL function search_contacts."""
    query = input("Enter search query (Name, Email, or Phone): ")
    conn = get_connection()
    cur = conn.cursor()
    
    cur.callproc('search_contacts', (query,))
    rows = cur.fetchall()
    
    print("\n--- Search Results ---")
    for row in rows:
        print(row)
        
    cur.close()
    conn.close()

def export_json():
    """DEFENSE: Fetches data and structures it into a dictionary before saving to JSON."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT c.name, c.email, CAST(c.birthday AS TEXT), g.name, p.phone, p.type
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        LEFT JOIN phones p ON c.id = p.contact_id
    """)
    rows = cur.fetchall()

    export_data = {}
    for row in rows:
        name, email, bday, group, phone, p_type = row
        if name not in export_data:
            export_data[name] = {"email": email, "birthday": bday, "group": group, "phones": []}
        if phone:
            export_data[name]["phones"].append({"phone": phone, "type": p_type})

    with open('export.json', 'w') as f:
        json.dump(export_data, f, indent=4)
    print("Data exported to export.json")
    
    cur.close()
    conn.close()

def import_json():
    """DEFENSE: Reads JSON. Asks user to skip or overwrite if a duplicate name is found."""
    try:
        with open('export.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("export.json not found!")
        return

    conn = get_connection()
    cur = conn.cursor()

    for name, info in data.items():
        cur.execute("SELECT id FROM contacts WHERE name = %s", (name,))
        existing = cur.fetchone()

        if existing:
            choice = input(f"Contact '{name}' already exists. [S]kip or [O]verwrite? ").lower()
            if choice == 's':
                continue
            elif choice == 'o':
                cur.execute("DELETE FROM contacts WHERE name = %s", (name,)) # Cascade deletes phones

        # Insert Group
        group_id = None
        if info['group']:
            cur.execute("INSERT INTO groups (name) VALUES (%s) ON CONFLICT (name) DO NOTHING", (info['group'],))
            cur.execute("SELECT id FROM groups WHERE name = %s", (info['group'],))
            group_id = cur.fetchone()[0]

        # Insert Contact
        cur.execute("""
            INSERT INTO contacts (name, email, birthday, group_id) 
            VALUES (%s, %s, %s, %s) RETURNING id
        """, (name, info['email'], info['birthday'], group_id))
        contact_id = cur.fetchone()[0]

        # Insert Phones
        for p in info['phones']:
            cur.execute("INSERT INTO phones (contact_id, phone, type) VALUES (%s, %s, %s)", 
                        (contact_id, p['phone'], p['type']))

    conn.commit()
    cur.close()
    conn.close()
    print("Import complete.")

def add_phone_procedure():
    name = input("Contact Name: ")
    phone = input("Phone Number: ")
    p_type = input("Type (home/work/mobile): ")
    conn = get_connection()
    cur = conn.cursor()
    try:
        # DEFENSE: Executing a stored procedure using the 'CALL' SQL command.
        cur.execute("CALL add_phone(%s, %s, %s)", (name, phone, p_type))
        conn.commit()
        print("Phone added successfully.")
    except Exception as e:
        print("Error:", e)
    cur.close()
    conn.close()

def move_group_procedure():
    name = input("Contact Name: ")
    group = input("New Group Name: ")
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("CALL move_to_group(%s, %s)", (name, group))
        conn.commit()
        print("Moved to group successfully.")
    except Exception as e:
        print("Error:", e)
    cur.close()
    conn.close()

def add_contact():
    name = input("Name: ")
    email = input("Email: ")
    birthday = input("Birthday (YYYY-MM-DD): ")
    group = input("Group (optional): ")

    conn = get_connection()
    cur = conn.cursor()

    try:
        group_id = None

        if group:
            cur.execute("""
                INSERT INTO groups (name)
                VALUES (%s)
                ON CONFLICT (name) DO NOTHING
            """, (group,))

            cur.execute("SELECT id FROM groups WHERE name=%s", (group,))
            result = cur.fetchone()
            if result:
                group_id = result[0]

        cur.execute("""
            INSERT INTO contacts (name, email, birthday, group_id)
            VALUES (%s, %s, %s, %s)
        """, (name, email, birthday, group_id))

        conn.commit()
        print("Contact added successfully!")

    except Exception as e:
        print("Error:", e)

    finally:
        cur.close()
        conn.close()

def main_menu():
    while True:
        print("\n=== Advanced PhoneBook TSIS 1 ===")
        print("1. Setup Database (Run SQL files)")
        print("2. View Contacts (Paginated & Filtered)")
        print("3. Search Contacts")
        print("4. Add Phone (Procedure)")
        print("5. Move to Group (Procedure)")
        print("6. Export to JSON")
        print("7. Import from JSON")
        print("8. Add Contact")
        print("0. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            run_sql_file('schema.sql')
            run_sql_file('procedures.sql')
        elif choice == '2': view_contacts_paginated()
        elif choice == '3': search_contacts()
        elif choice == '4': add_phone_procedure()
        elif choice == '5': move_group_procedure()
        elif choice == '6': export_json()
        elif choice == '7': import_json()
        elif choice == '8': add_contact()
        elif choice == '0': break
        else: print("Invalid choice.")

if __name__ == '__main__':
    main_menu()