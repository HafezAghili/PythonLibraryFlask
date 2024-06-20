from flask import Flask, render_template, request
from controller.user_controller import UserController

app = Flask(__name__, template_folder="view", static_folder="view/assets")

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/sign_in", methods=["POST"])
def sign_in():
    name = request.form.get("name")
    password = request.form.get("password")
    status, user = UserController.find_by_username_and_password(name, password)
    print(user)
    if status and user:
        return render_template("panel.html", user=user[0])
    else:
        return render_template("login-error.html")

@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        name = request.form.get("name")
        role = request.form.get("role")
        email = request.form.get("email")
        phone = request.form.get("phone")
        password = request.form.get("password")
        status, user = UserController.save(name, role, email, phone, password)

        if status and user:
            return render_template("login.html", user=user[0])

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
    user.id = id
    if status and user:
        return render_template("panel.html", user=user)

app.run(host='0.0.0.0', port=5000, debug=True)
