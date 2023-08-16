from sql_class import SQLClass


my_SQL = SQLClass("blueberry.db")

def create_cards():
    my_SQL.new_user("Lisa", "login", '310351')
    my_SQL.new_workspace("english", 1)
    my_SQL.new_table(name='words', workspace_id=1)

    my_SQL.new_card("dog", "собака", 1)
    my_SQL.new_card("cat", "кошка", 1)
    my_SQL.new_card("bird", "птица", 1)
    my_SQL.new_card("pig", "свинья", 1)
    my_SQL.new_card("rat", "крыса", 1)

def delete_user():
    my_SQL.delete_user(1)


# create_cards()
delete_user()