from flask import Flask, render_template, request
import urllib.parse
from sqlalchemy.orm import sessionmaker
from model.entity.user import User
from controller.user_controller import UserController
from sqlalchemy import create_engine

app = Flask(__name__)

username = "root"
password = "@Mir1379"
database_name = "Library"

encoded_password = urllib.parse.quote_plus(password)

connection_string = f"mysql+pymysql://{username}:{encoded_password}@localhost:3306/{database_name}"
engine = create_engine(connection_string)
Session = sessionmaker(bind=engine)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/sign_in", methods=["POST"])
def sign_in():
    name = request.form.get("name")
    password = request.form.get("password")
    status, users = UserController.find_by_username_and_password(name, password)
    if status and users:
        user = users[0]
        return render_template("panel.html", name=user.name, role=user.role, email=user.email, phone=user.phone)
    else:
        return render_template("login-error.html")



@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        password = request.form.get("password")

        new_user = User(name=name, role="user", email=email, phone=phone, password=password)

        session = Session()
        session.add(new_user)
        session.commit()

        return render_template("login.html", user=new_user)

    return render_template("sign-up.html")

@app.route("/edit-user", methods=["POST"])
def edit_user():
    id = int(request.form.get("id"))
    name = request.form.get("name")
    role = request.form.get("role")
    email = request.form.get("email")
    phone = request.form.get("phone")
    password = request.form.get("password")
    
    status, user = UserController.edit(id, name, role, email, phone, password)
    
    if status and user:
        return render_template("panel.html", user=user)
    else:
        return render_template("edit-error.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

































# from flask import Flask, render_template, request
# from sqlalchemy.orm import sessionmaker
# from model.entity.user import User
# from datetime import datetime
# from controller.user_controller import UserController
# from sqlalchemy import create_engine

# app = Flask(__name__)


# DATABASE_URL = "mysql+pymysql://username:password@localhost:3306/library"
# engine = create_engine(DATABASE_URL)

# Session = sessionmaker(bind=engine)


# @app.route("/")
# def login():
#     return render_template("login.html")

# @app.route("/sign_in", methods=["POST"])
# def sign_in():
#     name = request.form.get("name")
#     password = request.form.get("password")
#     status, user = UserController.find_by_username_and_password(name, password)
#     print(user)
#     if status and user:
#         return render_template("panel.html", user=user[0])
#     else:
#         return render_template("login-error.html")



# @app.route('/sign-up', methods=['GET', 'POST'])
# def sign_up():
#     if request.method == 'POST':
#         name = request.form['name']
#         role = request.form['role']
#         email = request.form['email']
#         phone = request.form['phone']
#         password = request.form['password']

#         new_user = User(name=name, role=role, email=email, phone=phone, password=password)

#         session = Session()
#         session.add(new_user)
#         session.commit()

#         return render_template("login.html", user=new_user)

#     return render_template("sign_up.html")


# @app.route("/edit-user", methods=["POST"])
# def edit_user():
#     id = int(request.form.get("id"))
#     name = request.form.get("name")
#     role = request.form.get("role")
#     email = request.form.get("email")
#     phone = request.form.get("phone")
#     password = request.form.get("password")
#     status, user = UserController.edit(id, name, role, email, phone, password)
#     user.id = id
#     if status and user:
#         return render_template("panel.html", user=user)

# app.run(host='0.0.0.0', port=5000, debug=True)














# @app.route("/sign-up", methods=["GET", "POST"])
# def sign_up():
#     if request.method == "POST":
#         name = request.form.get("name")
#         role = request.form.get("role")
#         email = request.form.get("email")
#         phone = request.form.get("phone")
#         password = request.form.get("password")
#         status, user = UserController.save(name, role, email, phone, password)

#         if status and user:
#             return render_template("login.html", user=user[0])

#     return render_template("sign-up.html")
