from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id:str, email:str, password:str, is_confirmed: int):
        self._id = id;
        self.email = email;
        self.password = password;
        self.is_confirmed = bool(is_confirmed)
        self.authenticated = False


    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False

    def get_id(self):
        return self._id
