from flask_app import app
from flask import render_template, redirect, request, session

from flask_app.models.friend import Friend

@app.route("/")
def index():
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", friends=friends)