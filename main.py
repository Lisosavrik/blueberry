from flask import Flask, jsonify, render_template, redirect, url_for, request, Response, flash, current_app
from flask_cors import CORS
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from flask_mail import Mail
from user_cl import User
from backend.sql_class import mySQl
from email_token import generate_token, confirm_token
from email_utils import send_email
from config import Config
from backend.extensions.login import login_manager


# move to init_login init_login()


app = Flask(
    __name__,
    static_folder="./client/vue-app/dist",
    template_folder="./client/vue-app/src/static",
    static_url_path="",
)

login_manager.init_app(app)

#what is from_object??? read about

app.config.from_object(Config)
mail = Mail(app)
mail.init_app(app)


def create_email(confirm_url: str):
    return(render_template("email.html", email_link=confirm_url))

def ErrorResponse(err_message: str): 
    return Response(err_message, 400, mimetype="application/json")

def OkMessage(ok_message: str):
    return jsonify(ok_message)

def render(page_name):
    return render_template(f"{page_name}.html")


@app.route("/", methods=["GET"])
def index():
    return current_app.send_static_file("index.html")




# move to blueprint authentication
@app.route('/api/log_in', methods=["POST"])
def login():
    data = request.get_json(force=True)
    login = data["login"]
    password = data["password"]
    

    user_id = mySQl.get_user_id_with_login_and_password(login, password)
    # Error: pass user_id to login_user()
    #what to do with load_user if it in the extensions/login.py???
    object_user = load_user(user_id)

    if object_user == None:
        # won't 
        flash('Login Unsuccessfull.')
    else:
        # Error: pass user_id to login_user()
        login_user(object_user, remember=True)
        return jsonify("oke!")





# move to blueprint authentication
@app.route('/api/sign_up', methods=["POST"])
def signup():
    data = request.get_json(force=True)
    name = data['name']
    login = data["login"]
    password = data["password"]

    account = mySQl.user_is_exict(log_in=login, password=password)
    
    
    if account:
        # will have to refactor frontend code
        # later with Lev
        return ErrorResponse("Account already exists")
    elif mySQl.correct_email(login) == False:
        # will have to refactor frontend code
        # later with Lev
        return ErrorResponse("Invalid email")
    elif mySQl.correct_password(password) == False:
        # will have to refactor frontend code
        # later with Lev
        return ErrorResponse("Invalid password")
    elif not name or not password or not login:
        # will have to refactor frontend code
        # later with Lev
        return ErrorResponse('Please fill out the form!')
    else:
        mySQl.new_user(user_name=name, log_in=login, password=password)

    logout_user()

    # Email logic
    token = generate_token(login, app)
    #creating cinfirm_url
    confirm_url = url_for("verification", token=token, _external=True)
    #read the email.html file? i think that doesnt work

    html_msg = create_email(confirm_url)
    subject = "Please confirm your email"

    send_email(login, subject, app, mail, html_msg)

    return jsonify("oke!")


# move to blueprint workspace
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
        # specify the reason why the request has failed:
        # return ErrorResponse("Wokrspace name is too short")
        return ErrorResponse("Wokrspace not added")

# move to blueprint table
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

# move to blueprint card
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

# move to blueprint workspace
@app.route("/api/workspace/delete/<workspace_id>", methods=["DELETE"])
@login_required
def delete_workspace(workspace_id: str):
    mySQl.delete_workspace(int(workspace_id))
    return OkMessage("ok")


# move to blueprint table
@app.route("/api/tables/delete/<table_id>", methods=["DELETE"])
@login_required
def delete_table(table_id: str):
    mySQl.delete_table(int(table_id))
    return OkMessage("ok")

# move to blueprint card
@app.route("/api/cards/delete/<card_id>", methods=["DELETE"])
@login_required
def delete_card(card_id: str):
    mySQl.delate_card(int(card_id))
    return OkMessage("ok")

# move to blueprint table
@app.route("/api/tables/move_table/<table_id>", methods=["POST"])
@login_required
def move_table(table_id:str):
    workspace_id = request.get_json(force=True)["workspace_id"]
    mySQl.move_table(int(table_id), int(workspace_id))

# move to blueprint card
@app.route("/api/cards/move_card/<card_id>", methods=["POST"])
@login_required
def move_card(card_id:str):
    table_id = request.get_json(force=True)["table_id"]
    mySQl.move_card(int(card_id), int(table_id))




# move to blueprint user
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


# move to blueprint authentication
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


@app.route("/send_email", methods=["GET"])
def test_send_email():
    send_email(
        to="kirill.o.amirov@gmail.com",
        subject="-",
        app=current_app,
        mail=mail,
        html_msg=create_email(123))
    
    return "OK"

if __name__ == "__main__":
    app.run(port=8000, debug=True)

# kirill.o.amirov@gmail.com
