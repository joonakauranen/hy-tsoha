from flask import Flask
from flask import redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from os import abort, getenv
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
app.secret_key = getenv("SECRET_KEY")
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create_topic")
def create_topic():
    return render_template("create_topic.html")

@app.route("/login",methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        sql = "SELECT password, id, role FROM users WHERE name=:name"
        result = db.session.execute(sql, {"name":username})
        user = result.fetchone()
        if not user:
            return redirect("/")
        if not check_password_hash(user[0], password):
            return redirect("/")
        session["user_id"] = user[1]
        session["user_name"] = username
        session["user_role"] = user[2]
        #session["csrf_token"] = os.urandom(16).hex()
        return redirect("/")

    return redirect("/")

@app.route("/logout")
def logout():
    del session["user_name"]
    del session["user_role"]
    del session["user_id"]
    return redirect("/")

@app.route("/register",methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        user = request.form["username"]
        pas = request.form["password"]
        rol = request.form["role"]
        hash_value = generate_password_hash(pas)
        sql = "INSERT INTO users (name, password, role) VALUES (:name, :password, :role)"
        db.session.execute(sql, {"name":user, "password":hash_value, "role":rol})
        db.session.commit()
        return redirect("/")

def user_id():
    return session.get("user_id", 0)

def require_role(role):
    if role > session.get("user_role", 0):
        abort(403)
