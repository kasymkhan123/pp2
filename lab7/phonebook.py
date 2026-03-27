import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    database="phonebook",
    user="postgres",
    port="5432",
    password="abilkosha"
)

cur = conn.cursor()


def create_table():
    cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        user_id SERIAL PRIMARY KEY,
        username VARCHAR(100) NOT NULL,
        phone VARCHAR(20) NOT NULL
    );
    """)
    conn.commit()


def insert_from_console():
    username = input("Enter username: ")
    phone = input("Enter phone: ")

    cur.execute(
        "INSERT INTO phonebook (username, phone) VALUES (%s, %s)",
        (username, phone)
    )
    conn.commit()


def insert_from_csv():
    with open("contacts.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)

        for row in reader:
            if len(row) == 2:
                username = row[0]
                phone = row[1]

                cur.execute(
                    "INSERT INTO phonebook (username, phone) VALUES (%s, %s)",
                    (username, phone)
                )

    conn.commit()


def show_all_contacts():
    cur.execute("SELECT * FROM phonebook ORDER BY user_id")
    rows = cur.fetchall()

    for row in rows:
        print(row)


def query_by_username():
    username = input("Enter username to search: ")

    cur.execute(
        "SELECT * FROM phonebook WHERE username ILIKE %s",
        ("%" + username + "%",)
    )
    rows = cur.fetchall()

    for row in rows:
        print(row)


def query_by_phone():
    phone = input("Enter phone to search: ")

    cur.execute(
        "SELECT * FROM phonebook WHERE phone = %s",
        (phone,)
    )
    rows = cur.fetchall()

    for row in rows:
        print(row)


def update_username():
    phone = input("Enter phone: ")
    new_username = input("Enter new username: ")

    cur.execute(
        "UPDATE phonebook SET username = %s WHERE phone = %s",
        (new_username, phone)
    )
    conn.commit()


def update_phone():
    username = input("Enter username: ")
    new_phone = input("Enter new phone: ")

    cur.execute(
        "UPDATE phonebook SET phone = %s WHERE username = %s",
        (new_phone, username)
    )
    conn.commit()


def delete_by_username():
    username = input("Enter username to delete: ")

    cur.execute(
        "DELETE FROM phonebook WHERE username = %s",
        (username,)
    )
    conn.commit()


def delete_by_phone():
    phone = input("Enter phone to delete: ")

    cur.execute(
        "DELETE FROM phonebook WHERE phone = %s",
        (phone,)
    )
    conn.commit()


create_table()

while True:
    print("\n1. Insert from console")
    print("2. Insert from CSV")
    print("3. Show all contacts")
    print("4. Search by username")
    print("5. Search by phone")
    print("6. Update username")
    print("7. Update phone")
    print("8. Delete by username")
    print("9. Delete by phone")
    print("0. Exit")

    choice = input("Choose: ")

    if choice == "1":
        insert_from_console()
    elif choice == "2":
        insert_from_csv()
    elif choice == "3":
        show_all_contacts()
    elif choice == "4":
        query_by_username()
    elif choice == "5":
        query_by_phone()
    elif choice == "6":
        update_username()
    elif choice == "7":
        update_phone()
    elif choice == "8":
        delete_by_username()
    elif choice == "9":
        delete_by_phone()
    elif choice == "0":
        break

cur.close()
conn.close()

