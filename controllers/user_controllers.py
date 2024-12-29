from models.user_models import UserModel


class UserController:
    def __init__(self):
        self.user_model = UserModel()

    def create_user(self, name, email):
        return self.user_model.create(name, email)

    def get_users(self):
        return self.user_model.read_all()

    def update_user(self, user_id, name, email):
        return self.user_model.update(user_id, name, email)

    def delete_user(self, user_id):
        return self.user_model.delete(user_id)
