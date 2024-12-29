from controllers.user_controllers import UserController
from views.menu_view import MenuView


def main():
    user_controller = UserController()
    view = MenuView()

    while True:
        view.display_menu()
        choice = view.get_input("Enter choice: ")

        if choice == "1":
            name = view.get_input("Enter name: ")
            email = view.get_input("Enter email: ")
            if name and email:
                result = user_controller.create_user(name, email)
                view.display_message(result["message"])
            else:
                view.display_message("Error: Name and email cannot be empty.")

        elif choice == "2":
            users = user_controller.get_users()
            view.display_users(users)

        elif choice == "3":
            try:
                user_id = int(view.get_input("Enter user ID to update: "))
                name = view.get_input("Enter new name: ")
                email = view.get_input("Enter new email: ")
                if name and email:
                    result = user_controller.update_user(user_id, name, email)
                    view.display_message(result["message"])
                else:
                    view.display_message("Error: Name and email cannot be empty.")
            except ValueError:
                view.display_message("Error: User ID must be an integer.")

        elif choice == "4":
            try:
                user_id = int(view.get_input("Enter user ID to delete: "))
                result = user_controller.delete_user(user_id)
                view.display_message(result["message"])
            except ValueError:
                view.display_message("Error: User ID must be an integer.")

        elif choice == "5":
            view.display_message("Exiting the program. Goodbye!")
            break

        else:
            view.display_message("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
