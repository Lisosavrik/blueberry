import sqlite3
import datetime 
from datetime import timedelta
from validate_email import validate_email

class SQLClass():
    def __init__(self, db_path: str):
        self.db_path = db_path

    def get_today(self):
        return datetime.datetime.today()

    def db_connect(self):
        self.db: sqlite3.Connection = sqlite3.connect(self.db_path)
        self.cursor: sqlite3.Cursor = self.db.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON")

    def update_db(self):
        self.db.commit()
    
    def close_db(self):
        self.db.close()

    def new_user(self, user_name: str, log_in: str, password: str):
        self.db_connect()

        self.cursor.execute(f"""
            INSERT INTO Users(name, log_in, password) VALUES('{user_name}', '{log_in}', '{password}')
            """)
        
        self.update_db()
        self.close_db()

    def new_workspace(self, name: str, user_id: int):
        self.db_connect()

        self.cursor.execute(f"""
            INSERT INTO Workspaces(name, user_id) VALUES('{name}', '{user_id}')
            """)
        
        self.update_db()
        self.close_db()

    def new_table(self, name:str, workspace_id:int):
        self.db_connect()

        self.cursor.execute(f"""
            INSERT INTO Tables(name, workspace_id) VALUES('{name}', '{workspace_id}')
            """)
        
        self.update_db()
        self.close_db()

    def new_card(self, key:str, value:str, table_id:int):
        today = self.get_today().strftime("%d-%m-%Y")

        self.db_connect()


        self.cursor.execute(f"""
            INSERT INTO Cards(key, value, training_date, color, next_well, next_very_well, table_id) 
            VALUES('{key}', '{value}', '{today}', "red", 3, 5, '{table_id}')
            """)
        
        self.update_db()
        self.close_db()

    def user_is_exict(self, log_in: str, password: str):
        self.db_connect()

        self.cursor.execute(f"SELECT user_id FROM Users WHERE log_in ='{log_in}'")
        arr = self.cursor.fetchall()
        res = arr[0] if (len(arr) > 0) else ()
        self.close_db()

        if len(res) == 0:
            return False
        else:
            return True

        

    def delete_user(self, user_id):
        self.db_connect()

        self.cursor.execute(f"DELETE FROM Users WHERE user_id='{user_id}'")

        self.update_db()
        self.close_db()

    def delete_workspace(self, workspace_id):
        self.db_connect()

        self.cursor.execute(f"DELETE FROM Workspaces WHERE workspace_id='{workspace_id}")

        self.update_db()
        self.close_db()

    def delete_table(self, table_id):
        self.db_connect()

        self.cursor.execute(f"DELETE FROM Tables WHERE table_id='{table_id}'")

        self.update_db()
        self.close_db()

    def delate_card(self, card_id):
        self.db_connect()

        self.cursor.execute(f"DELETE FROM Cards WHERE card_id='{card_id}'")
        self.update_db()
        self.close_db()

    def move_card(self, card_id, table_id):
        self.db_connect()
            
        self.cursor.execute(f"UPDATE Cards SET table_id={table_id} WHERE card_id='{card_id}'")

        self.update_db()
        self.close_db()

    def move_table(self, table_id, workspace_id):
        self.db_connect()

        self.cursor.execute(f"UPDATE tables SET workspace_id='{workspace_id}' WHERE table_id='{table_id}'")

        self.update_db()
        self.close_db()

    def update_card (self, button_term, card_id):
        today = self.get_today()

        training_day = today+timedelta(days=button_term)
        color = "yellow"

        str_training_day = training_day.strftime("%d-%m-%Y")
        self.cursor.execute(f"UPDATE Cards SET training_date='{str_training_day}', color='{color}' WHERE card_id='{card_id}'")
        self.update_db()

    def training_now(self):
        today = self.get_today().strftime('%d-%m-%Y')
        
        self.cursor.execute(f"SELECT * FROM Cards WHERE training_date='{today}'")
        res = self.cursor.fetchall()

        return res

    def update_well(self, term: int, card_id: int):
        self.db_connect()
        self.cursor.execute(f"SELECT * FROM Cards WHERE card_id = '{card_id}'")
        card = self.cursor.fetchall()[0]
        if term >=3:
            new_nxt_well = int(card[5] + (card[5] * 0.2))
            new_nxt_very_well = int(card[6] + (card[6] * 0.2))
        else:
            new_nxt_well = 3
            new_nxt_very_well = 5

        self.cursor.execute(f"UPDATE Cards SET next_well='{new_nxt_well}', next_very_well='{new_nxt_very_well}' WHERE card_id='{card_id}'")
        self.update_db()

    def get_user_id_with_login_and_password(self, login: str, password: str):
        self.db_connect()

        self.cursor.execute(f"SELECT id FROM Users WHERE log_in='{login}' AND password={password}")

        user_data = self.cursor.fetchone()
        self.close_db()
        user_data = user_data if len(user_data) != 0 else [None]
        return user_data[0]

    def select_by_id(self, user_id):

        self.db_connect()

        self.cursor.execute(f"SELECT * FROM User WHERE user_id='{user_id}'")
        user = self.cursor.fetchone()
        self.close_db()
        return user

    def correct_email(self, email:str):
        return bool(validate_email(email))

    # def validate_credentials():
    #     return "fadfksaokf"
    #     return None

    def correct_password(self, password:str):
        is_len = True if len(password) >= 7 else False
        is_one_low = False
        is_one_up = False
        is_one_numeric = False
        for literal in password:
            if literal.islower():
                is_one_low = True
            elif literal.isupper():
                is_one_up = True
            elif literal.isnumeric():
                is_one_numeric = True
        
        if is_len and is_one_low and is_one_up and is_one_numeric:
            return True 
        else:
            return False

    def get_workspaces(self, user_id:int):
        self.db_connect()
        self.cursor.execute(f"SELECT * FROM Workspaces WHERE user_id={user_id}")
        arr = self.cursor.fetchall()
        res = arr[0] if (len(arr) > 0) else ()
        self.close_db()
        return res


    def get_tables(self, workspace_id:int):
        self.db_connect()
        self.cursor.execute(f"SELECT * FROM Tables WHERE workspace_id={workspace_id}")
        arr = self.cursor.fetchall()
        res = arr[0] if (len(arr) > 0) else ()
        self.close_db()
        return res

    def get_cards(self, table_id:int):
        self.db_connect()
        self.cursor.execute(f"SELECT * FROM Carts WHERE table_id={table_id}")
        arr = self.cursor.fetchall()
        res = arr[0] if (len(arr) > 0) else ()
        self.close_db()
        return res