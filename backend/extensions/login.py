from flask_login import LoginManager
from backend.sql_class import mySQl
from user_cl import User

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    user = mySQl.select_by_id(user_id=user_id)
    if user == None:
        return None
    else:
        return User(user[0], user[2], user[3], user[4])