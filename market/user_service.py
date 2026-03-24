from .user import User

class UserService:
    def __init__(self):
        self.users = []
        self.current_user = None

    def create_user(self, user_id, name):
        user = User(user_id, name)
        self.users.append(user)
        return user

    def login(self, user_id):
        for u in self.users:
            if u.user_id == user_id:
                self.current_user = u
                return f"{u.name} giriş yaptı."
        return "Kullanıcı bulunamadı."

    def logout(self):
        self.current_user = None
        return "Çıkış yapıldı."

    def get_current_user(self):
        return self.current_user
    