import sqlite3


class UserModel:
    def __init__(self, db_path="users.db"):
        self.db_path = db_path
        self.init_db()

    def init_db(self):
        """
        Khởi tạo cơ sở dữ liệu và bảng nếu chưa tồn tại.
        """
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL UNIQUE,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )''')
        conn.commit()
        conn.close()

    def create(self, name, email):
        """
        Thêm người dùng mới vào cơ sở dữ liệu.
        """
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        try:
            c.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
            conn.commit()
            return {"success": True, "message": "User created successfully."}
        except sqlite3.IntegrityError as e:
            return {"success": False, "message": f"Error: {e} (Có thể email đã tồn tại)"}
        finally:
            conn.close()

    def read_all(self):
        """
        Đọc danh sách tất cả người dùng.
        """
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("SELECT * FROM users")
        users = c.fetchall()
        conn.close()
        return users

    def update(self, user_id, name, email):
        """
        Cập nhật thông tin người dùng.
        """
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (name, email, user_id))
        conn.commit()
        affected_rows = c.rowcount
        conn.close()
        if affected_rows == 0:
            return {"success": False, "message": "User ID not found."}
        return {"success": True, "message": "User updated successfully."}

    def delete(self, user_id):
        """
        Xóa người dùng theo ID.
        """
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()
        affected_rows = c.rowcount
        conn.close()
        if affected_rows == 0:
            return {"success": False, "message": "User ID not found."}
        return {"success": True, "message": "User deleted successfully."}
