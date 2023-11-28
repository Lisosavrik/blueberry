from flask import Flask, jsonify, render_template, redirect, url_for, request, Response, Blueprint, flash
from flask_cors import CORS
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from flask_mail import Mail
from user_cl import User
from backend.sql_class import SQLClass
from email_token import generate_token, confirm_token
from email_utils import send_email
from config import Config


mySQl = SQLClass('blueberry.db')

login_manager = LoginManager()


app = Flask(__name__)
login_manager.init_app(app)
app.config.from_object(Config())
mail = Mail(app)


def create_email(confirm_url):
    with open("static/email.html", "r") as file:
        file_text = file.read()
    
    return file_text.format(email_link=confirm_url)

def ErrorResponse(err_message: str): 
    return Response(err_message, 400, mimetype="application/json")

def OkMessage(ok_message: str):
    return jsonify(ok_message)

def render(page_name):
    return render_template(f"{page_name}.html")


@app.route("/", methods=["GET"])
def index():
    return render("index")

@app.route("/have_to_confirm", methods=["GET"])
def confirm():
    return render('have_to_confirm')



@app.route("/sign_up", methods=["GET"])
def signup_page():
    return render("sign_up")

@app.route('/log_in', methods=["GET"])
def login_page():
    1
    if current_user.is_authenticated:
        return redirect(url_for('training_page'))
    else:
        return render("log_in")

@app.route("/workspaces", methods=["GET"])
@login_required
def workspaces_page():
    return render("workspaces")


@app.route("/training", methods=["GET"])
@login_required
def training_page():
    return render("training")



@login_manager.user_loader
def load_user(user_id):
    user = mySQl.select_by_id(user_id=user_id)
    if user == None:
        return None
    else:
        return User(user[0], user[2], user[3], user[4])



@app.route('/api/log_in', methods=["POST"])
def login():
    data = request.get_json(force=True)
    login = data["login"]
    password = data["password"]
    
    user_id = mySQl.get_user_id_with_login_and_password(login, password)
    object_user = load_user(user_id)

    if object_user == None:
        flash('Login Unsuccessfull.')
    else:
        login_user(object_user, remember=True)
        return jsonify("oke!")






@app.route('/api/sign_up', methods=["POST"])
def signup():
    data = request.get_json(force=True)
    name = data['name']
    login = data["login"]
    password = data["password"]

    account = mySQl.user_is_exict(log_in=login, password=password)
    
    
    if account:
        return ErrorResponse("Account already exists")
    elif mySQl.correct_email(login) == False:
        return ErrorResponse("Invalid email")
    elif mySQl.correct_password(password) == False:
        return ErrorResponse("Invalid password")
    elif not name or not password or not login:
        return ErrorResponse('Please fill out the form!')
    else:
        mySQl.new_user(user_name=name, log_in=login, password=password)

    logout_user()
    token = generate_token(login, app)
    confirm_url = url_for("verification", token=token, _external=True)
    text_with_url = create_email(confirm_url)
    subject = "Please confirm your email"

    send_email(login, subject, text_with_url, app, mail)

    return jsonify("oke!")


@app.route("/api/add_workspace", methods=["POST"])
@login_required
def add_workspace():
    data = request.get_json(force=True)
    title = data["title"]

    user_id = current_user.get_id()
    if len(title) >= 1:
        new_workspace_id = mySQl.new_workspace(title, user_id)
        return jsonify({"workspace_id": new_workspace_id})
    else:
        return  ErrorResponse("Wokrspace not added")
    

@app.route("/api/add_table", methods=['POST'])
@login_required
def add_table():
    data = request.get_json(force=True)
    title = data["title"]
    workspace_id = data["workspace_id"]
    if len(title) >= 1 and workspace_id != None:
        new_table_id = mySQl.new_table(title, workspace_id)
        return jsonify({"table_id": new_table_id})
    else:
        return  ErrorResponse("Table not added")


@app.route("/api/add_card", methods=['POST'])
@login_required
def add_card():
    data = request.get_json(force=True)
    key = data["key"]
    value = data["value"]
    table_id = data["table_id"]

    if len(key) >=1 and len(value) >= 1:
        new_card_id = mySQl.new_card(key, value, table_id)
        today  = mySQl.get_today()
        return {"card_id": new_card_id, "today": today}
    else:
        return  ErrorResponse("card not added")


@app.route("/api/workspace/delete/<workspace_id>", methods=["DELETE"])
@login_required
def delete_workspace(workspace_id: str):
    mySQl.delete_workspace(int(workspace_id))
    return OkMessage("ok")


@app.route("/api/tables/delete/<table_id>", methods=["DELETE"])
@login_required
def delete_table(table_id: str):
    mySQl.delete_table(int(table_id))
    return OkMessage("ok")

@app.route("/api/cards/delete/<card_id>", methods=["DELETE"])
@login_required
def delete_card(card_id: str):
    mySQl.delate_card(int(card_id))
    return OkMessage("ok")


@app.route("/api/tables/move_table/<table_id>", methods=["POST"])
@login_required
def move_table(table_id:str):
    workspace_id = request.get_json(force=True)["workspace_id"]
    mySQl.move_table(int(table_id), int(workspace_id))


@app.route("/api/cards/move_card/<card_id>", methods=["POST"])
@login_required
def move_card(card_id:str):
    table_id = request.get_json(force=True)["table_id"]
    mySQl.move_card(int(card_id), int(table_id))





@app.route("/api/user/get_workspaces_with_tables_and_cards", methods=["GET"])
@login_required
def get_workspaces():
    user_id = current_user.get_id()
    workspaces = mySQl.get_workspaces(int(user_id))
    tables = {}
    cards = {}

    for workspace in workspaces:
        workspace_id = workspace["id"]
        tables[f"{workspace_id}"] = mySQl.get_tables(workspace_id)

        for table in tables[f'{str(workspace_id)}']:
            table_id = table["id"]
            cards[f"{table_id}"] = mySQl.get_cards(table_id)

    
    return jsonify({"workspaces": workspaces, "tables": tables, "cards": cards})



@app.route("/confirm/<token>", methods=["GET"])
def verification(token: str):
    email = confirm_token(token, app=app)
    if not email: return jsonify("link not valid")
    user = mySQl.get_user_by_email(email)
    if user != None:
        mySQl.update_condirmed(user["id"])
        return render('email_verification')
    else:
        return ErrorResponse("There is no user in database")





if __name__ == "__main__":
    app.run(port=8000, debug=True)
    login_manager.init_app(app)
