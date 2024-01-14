from flask import Flask
from flask import render_template
from datetime import datetime
from . import app

@app.route("/")
def home():
    print("hello")
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")