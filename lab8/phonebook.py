from connect import get_connection

def create_table(cur, conn):
    cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        user_id SERIAL PRIMARY KEY,
        username VARCHAR(100),
        surname VARCHAR(100),
        phone VARCHAR(20)
    );
    """)
    conn.commit()


def call_function(cur, query):
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)


def call_procedure(cur, conn, query):
    cur.execute(query)
    conn.commit()


def main():
    conn = get_connection()
    cur = conn.cursor()

    create_table(cur, conn)

    while True:
        print("\n1. Search (pattern)")
        print("2. Pagination")
        print("3. Upsert user")
        print("4. Bulk insert")
        print("5. Delete")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            pattern = input("Enter pattern: ")
            call_function(cur, f"SELECT * FROM search_phonebook('{pattern}')")

        elif choice == "2":
            limit = input("Limit: ")
            offset = input("Offset: ")
            call_function(cur, f"SELECT * FROM get_phonebook_page({limit}, {offset})")

        elif choice == "3":
            name = input("Name: ")
            surname = input("Surname: ")
            phone = input("Phone: ")
            call_procedure(cur, conn,
                f"CALL upsert_user('{name}', '{surname}', '{phone}')"
            )

        elif choice == "4":
            names = ["Ali", "John"]
            surnames = ["A", "B"]
            phones = ["12345", "bad_phone"]

            call_procedure(cur, conn,
                f"""
                CALL insert_many_users(
                    ARRAY{names},
                    ARRAY{surnames},
                    ARRAY{phones}
                )
                """
            )

        elif choice == "5":
            val = input("Enter username or phone: ")
            call_procedure(cur, conn,
                f"CALL delete_user('{val}')"
            )

        elif choice == "0":
            break

    cur.close()
    conn.close()


main()