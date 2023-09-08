import os

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session

# from helpers import apology

# Configure Application
app = Flask(__name__)

# Ensure templates are auto reloded
app.config["TEMPLATES_AUTO_RELOD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

link = ""
key = "landing"

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/register_page", methods=["GET", "POST"])
def register_page():
    if request.method == "GET":
        return render_template('register.html')
    global link
    link = request.form.get('link')
    return render_template('register.html')

@app.route("/register", methods=["GET", "POST"])
def register():
    session.clear()

    if request.method == "GET":
        return render_template("register.html")
    name = request.form.get('name')
    sch_id = request.form.get('sch_id')

    if link == key:
        return render_template("landing.html", name=name)
    return render_template('fail.html')

@app.route("/retry")
def retry():
    return render_template("index.html")