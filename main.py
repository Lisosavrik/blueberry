from flask import Flask, jsonify, render_template, redirect, url_for, request, Response, Blueprint, flash
from flask_cors import CORS
# from flask import globals
from flask_login import LoginManager, current_user, login_required, login_user
from user_cl import User
from backend.sql_class import SQLClass


mySQl = SQLClass('blueberry.db')

login_manager = LoginManager()

app = Flask(__name__)

def ErrorResponse(err_message: str): 
    return Response(err_message, 400, mimetype="application/json")

def OkMessage(ok_message: str):
    return Response(ok_message, 200, mimetype="application/json")

@app.route("/")
def index():
    return render_template("index.html")

@login_manager.user_loader
def load_user(user_id):
    user = mySQl.select_by_id(user_id=user_id)
    if user == None:
        return None
    else:
        return User(user[0], user[2], user[3])

@app.route('/log_in', methods=["GET"])
def login_page():
    if current_user.is_authenticated:
        return redirect(url_for('training'))
    else:
        return render_template("log_in.html")

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
        return redirect(url_for("training"))


@app.route("/sign_up", methods=["GET"])
def signup_page():
    return render_template("sign_up.html")

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

    return jsonify("oke!")


@app.route("/api/add_workspace", methods=["POST"])
@login_required
def add_workspace():
    data = request.get_json(force=True)
    title = data["title"]
    user_id = current_user.get_id()
    if len(title) >= 1:
        mySQl.new_workspace(title, user_id)
        return OkMessage("Workspace added")
    else:
        return  ErrorResponse("Wokrspace not added")
    

@app.route("/api/add_table", methods=['POST'])
@login_required
def add_table():
    data = request.get_json(force=True)
    title = data["title"]
    workspace_id = data["workspace_id"]
    if len(title) >= 1 and workspace_id != None:
        mySQl.new_table(title, workspace_id)
        return OkMessage("Table added")
    else:
        return  ErrorResponse("Table not added")


@app.route("/api/add_table", methods=['POST'])
@login_required
def add_card():
    data = request.get_json(force=True)
    key = data["key"]
    value = data["value"]
    table_id = data["table_id"]

    if len(key) >=1 and len(value) >= 1:
        mySQl.new_card(key, value, table_id)
        return OkMessage("card added")
    else:
        return  ErrorResponse("card not added")


@app.route("/api/workspace/delete/<workspace_id>", methods=["DELETE"])
@login_required
def delete_workspace(workspace_id: str):
    mySQl.delete_workspace(int(workspace_id))


@app.route("/api/tables/delete/<table_id>", methods=["DELETE"])
@login_required
def delete_table(table_id: str):
    mySQl.delete_workspace(int(table_id))

@app.route("/api/cards/delete/<card_id>", methods=["DELETE"])
@login_required
def delete_card(card_id: str):
    mySQl.delete_workspace(int(card_id))


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


# workspaceId = fetch(...)
# workspace.on("click", () => {
#     fetch(`localhost:5000/api/workspace/get_tables/workspace_id=${workspaceId}`)
# })
# fetch("localhost:5000/api/workspace/get_tables/workspace_id=5")
# @app.route("/api/workspace/get_tables/workspace_id=<workspace_id>", methods=["GET"])
# def get_tables(workspace_id: str):
#     return jsonify(mySQl.get_tables(int(workspace_id)))

@app.route("/api/user/get_workspaces", methods=["GET"])
@login_required
def get_workspaces():
    user_id = current_user.get_id()
    return jsonify(mySQl.get_workspaces(int(user_id)))

@app.route("/api/workspaces/<workspace_id>", methods=["GET"])
@login_required
def get_tables(workspace_id:str):
    return jsonify(mySQl.get_tables(int(workspace_id)))

@app.route("/api/tables/<table_id>", methods=["GET"])
@login_required
def get_cards(table_id:str):
    return jsonify(mySQl.get_cards(int(table_id)))



if __name__ == "__main__":
    app.run(port=8000, debug=True)

login_manager.init_app(app)
