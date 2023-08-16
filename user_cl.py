from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id:str, email:str, password:str):
        self._id = id;
        self.email = email;
        self.password = password;
        self.authenticated = False

    def is_authenticated(self):
        return self.authenticated
    
    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False

    def get_id(self):
        return self._id
