from flask import render_template, redirect, url_for, request
from application import app, db
from application.models import Cars
from application.models import Review
from application import app, db

@app.route("/")
@app.route("/home")
def home():

    return render_template("home.html")

@app.route("/about")
def about():

    return render_template('about.html', title='about')

# @app.route("/test")
# def test():
    
#     return render_template("home.html")

    