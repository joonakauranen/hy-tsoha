import secrets
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
    user = user_id()
    favorites = messages.get_favorites(user)
    return render_template("index.html", topics = topics, favorites = favorites)

@app.route("/new_topic")
def create_topic():
    return render_template("new_topic.html")

@app.route("/new_message/<string:topic_id>")
def new_message(topic_id):
    return render_template("new_message.html", topic_id = topic_id)

@app.route("/messages/<string:id>")
def mes(id):
    topic_messages = messages.get_messages(id)
    return render_template("messages.html", topic_messages = topic_messages, topic_id = id)

@app.route("/create_topic", methods=["POST"])
def create():
    token = request.form["csrf_token"]
    csrf_check(token)
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
        session["csrf_token"] = secrets.token_hex(16)
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
        if len(user) == 0 or len(pas) == 0 or len(rol) == 0:
            return render_template("error.html", message="Rekisteröityminen epäonnistui. Varmista, että mikään kentistä ei ole tyhjä")
        hash_value = generate_password_hash(pas)
        sql = "INSERT INTO users (name, password, role) VALUES (:name, :password, :role)"
        db.session.execute(sql, {"name":user, "password":hash_value, "role":rol})
        db.session.commit()
        return redirect("/")

@app.route("/create_message/<string:topic_id>",methods=["POST"])
def create_message(topic_id):
    token = request.form["csrf_token"]
    csrf_check(token)
    content = request.form["content"]
    if len(content) == 0:
        return render_template("error.html", message="Viestin lähettäminen epäonnistui. Varmista, että viesti ei ole tyhjä")
    user = user_id()
    topic_messages = messages.new_message(content, user, topic_id)
    return render_template("messages.html", topic_messages=topic_messages, topic_id = topic_id)


@app.route("/search_messages", methods=["POST"])
def search():
    token = request.form["csrf_token"]
    csrf_check(token)
    keyword = request.form["content"]
    messages_found = messages.search_messages(keyword)
    return render_template("search_results.html", messages_found = messages_found, keyword = keyword)

@app.route("/search")
def create_search():
    return render_template("search_messages.html")

@app.route("/new_favorite/<string:topic_id>/<string:topic>")
def new_favorite(topic_id, topic):
    return render_template("new_favorite.html", topic_id = topic_id, topic = topic)

@app.route("/create_favorite/<string:topic_id>/<string:topic>",methods=["POST"])
def create_favorite(topic_id, topic):
    token = request.form["csrf_token"]
    csrf_check(token)
    user = user_id()
    if messages.new_favorite(topic, user, topic_id):
        return redirect("/")

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

def csrf_check(token):
    if session["csrf_token"] != token:
        abort(403)
