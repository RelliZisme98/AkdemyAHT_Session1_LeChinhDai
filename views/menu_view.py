class MenuView:
    @staticmethod
    def display_menu():
        print("\n--- User Management ---")
        print("1. Create User")
        print("2. Read Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Exit")

    @staticmethod
    def get_input(prompt):
        return input(prompt).strip()

    @staticmethod
    def display_users(users):
        if users:
            print("\n--- User List ---")
            for user in users:
                print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}, Created At: {user[3]}")
        else:
            print("No users found.")

    @staticmethod
    def display_message(message):
        print(message)
