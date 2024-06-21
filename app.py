from flask import Flask, render_template, request, redirect, url_for, session
import urllib.parse
from sqlalchemy.orm import sessionmaker
from model.entity.user import User
from model.entity.book import Book
from model.entity.loan import Loan
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

# @app.route("/")
# def login():
#     return render_template("login.html")

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form.get("name")
        password = request.form.get("password")
        session_db = Session()
        user = session_db.query(User).filter_by(name=name, password=password).first()
        if user:
            session['user_id'] = user.id  
            session['username'] = user.name  
            return redirect(url_for("loans"))
        else:
            return "Login failed"
    return render_template("login.html")

@app.route("/panel", methods=["POST"])
def panel():
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


@app.route("/books", methods=["GET", "POST"])
def books():
    session = Session()
    if request.method == "POST":
        title = request.form.get("title")
        author = request.form.get("author")
        pubdate = request.form.get("pubdate")
        language = request.form.get("language")
        isbn = request.form.get("isbn")

        new_book = Book(title=title, author=author, pubdate=pubdate, language=language, isbn=isbn)
        session.add(new_book)
        session.commit()
        return redirect(url_for("books"))
    
    books = session.query(Book).all()
    return render_template("books.html", books=books)

# @app.route("/loans", methods=["GET", "POST"])
# def loans():
#     session = Session()
#     if request.method == "POST":
#         user_id = request.form.get("user_id")
#         book_id = request.form.get("book_id")
#         loan_date = datetime.now()
        
#         new_loan = Loan(user_id=user_id, book_id=book_id, loan_date=loan_date)
#         session.add(new_loan)
#         session.commit()
#         return redirect(url_for("loans"))

#     loans = session.query(Loan).all()
#     books = session.query(Book).all()
#     return render_template("loans.html", loans=loans, books=books)


@app.route("/loans", methods=["GET", "POST"])
def loans():
    session_db = Session()
    if request.method == "POST":
        user_id = request.form.get("user_id") 
        book_id = request.form.get("book_id")
        loan_date = request.form.get("loan_date")
        
        new_loan = Loan(user_id=user_id, book_id=book_id, loandate=loan_date)
        session_db.add(new_loan)
        session_db.commit()
        return redirect(url_for("loans"))

    loans = session_db.query(Loan).all()
    books = session_db.query(Book).all()
    users = session_db.query(User).all()
    return render_template("loans.html", loans=loans, books=books, users=users)

# @app.route("/loans", methods=["GET", "POST"])
# def loans():
#     session_db = Session()
#     if request.method == "POST":
#         user_id = session.get('user_id')  # گرفتن user_id از session
#         book_id = request.form.get("book_id")
#         loandate = request.form.get("loandate")
        
#         new_loan = Loan(user_id=user_id, book_id=book_id, loandate=loandate)
#         session_db.add(new_loan)
#         session_db.commit()
#         return redirect(url_for("loans"))

#     loans = session_db.query(Loan).all()
#     books = session_db.query(Book).all()
#     return render_template("loans.html", loans=loans, books=books)

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
