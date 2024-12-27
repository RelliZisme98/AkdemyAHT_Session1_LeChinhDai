import sqlite3

def init_db():
    """
    Khởi tạo cơ sở dữ liệu và bảng users nếu chưa tồn tại.
    """
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )''')
    conn.commit()
    conn.close()


def create_user(name, email):
    """
    Thêm người dùng mới vào cơ sở dữ liệu.
    """
    try:
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        print("User created successfully.")
    except sqlite3.IntegrityError as e:
        print(f"Error: {e} (Có thể email đã tồn tại)")
    finally:
        conn.close()


def read_users():
    """
    Đọc và trả về danh sách tất cả người dùng từ cơ sở dữ liệu.
    """
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    conn.close()
    return users


def update_user(user_id, name, email):
    """
    Cập nhật thông tin người dùng dựa vào ID.
    """
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (name, email, user_id))
    conn.commit()
    if c.rowcount == 0:
        print("Error: User ID not found.")
    else:
        print("User updated successfully.")
    conn.close()


def delete_user(user_id):
    """
    Xóa người dùng dựa vào ID.
    """
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    if c.rowcount == 0:
        print("Error: User ID not found.")
    else:
        print("User deleted successfully.")
    conn.close()


def main():
    """
    Menu chính cho phép thực hiện các chức năng CRUD.
    """
    init_db()
    while True:
        print("\n--- User Management ---")
        print("1. Create User")
        print("2. Read Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ").strip()
            email = input("Enter email: ").strip()
            if name and email:
                create_user(name, email)
            else:
                print("Error: Name and email cannot be empty.")
        elif choice == "2":
            users = read_users()
            if users:
                print("\n--- User List ---")
                for user in users:
                    print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}, Created At: {user[3]}")
            else:
                print("No users found.")
        elif choice == "3":
            try:
                user_id = int(input("Enter user ID to update: ").strip())
                name = input("Enter new name: ").strip()
                email = input("Enter new email: ").strip()
                if name and email:
                    update_user(user_id, name, email)
                else:
                    print("Error: Name and email cannot be empty.")
            except ValueError:
                print("Error: User ID must be an integer.")
        elif choice == "4":
            try:
                user_id = int(input("Enter user ID to delete: ").strip())
                delete_user(user_id)
            except ValueError:
                print("Error: User ID must be an integer.")
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
