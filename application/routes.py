from flask import render_template, redirect, url_for, request
from application import app, db
from application.models import Cars
from application.models import Review
from application import app, db

@app.route("/")
@app.route("/home")
def home():
    carData = Cars.query.all()
    return render_template("home.html", title='Home', cars=carData)

@app.route("/about")
def about():

    return render_template('about.html', title='about')

@app.route('/reviews/<int:id>')
def reviews(id):
    carryviews = Review.query.filter_by(car_id=id).all()
    return render_template('reviews.html', title='review', reviews=carryviews)   


    