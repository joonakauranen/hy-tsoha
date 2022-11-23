from app import app
from flask import redirect, render_template, request, session
from os import abort
from werkzeug.security import check_password_hash, generate_password_hash
from db import db
import messages

@app.route("/")
def index():
    sql = "SELECT id, topic, created_at FROM topics ORDER BY id DESC"
    result = db.session.execute(sql)
    topics = result.fetchall()
    return render_template("index.html", topics = topics)

@app.route("/new")
def create_topic():
    return render_template("new.html")

@app.route("/new_message/<string:topic_id>")
def new_message(topic_id):
    return render_template("new_message.html", topic_id = topic_id)

@app.route("/messages/<string:id>")
def mes(id):
    topic_messages = messages.get_messages(id)
    return render_template("messages.html", topic_messages=topic_messages, topic_id=id)

@app.route("/create_topic", methods=["POST"])
def create():
    content = request.form["content"]
    user = user_id()
    if messages.add_topic(content, user):
        return redirect("/")
    else:
        return render_template("error.html", message="Aiheen luominen epäonnistui. Varmista, että otsikko ei ole tyhjä")

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

@app.route("/create_message/<string:topic_id>",methods=["POST"])
def create_message(topic_id):
    content = request.form["content"]
    user = user_id()
    if messages.new_message(content, user, topic_id):
        return render_template("messages.html", topic_id=topic_id)
    else:
        return render_template("error.html", message="Viestin lähettäminen epäonnistui. Varmista, että viestikenttä ei ole tyhjä.")
    

def user_id():
    return session.get("user_id", 0)

def user_name():
    return session.get("user_name", 0)

def user_role(role):
    if role > 0:
        return True
    return False

def require_role(role):
    if role > session.get("user_role", 0):
        abort(403)
