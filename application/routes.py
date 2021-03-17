from flask import render_template, redirect, url_for, request
from application import app, db
from application.models import Cars, Review, UpdateReview, AddCar, DeleteCar
from application import app, db

@app.route("/")
@app.route("/home")
def home():
    carData = Cars.query.all()

    return render_template("home.html", title='Home', cars=carData)

@app.route("/about")
def about():

    return render_template('about.html', title='about')

@app.route("/addcar", methods=['GET', 'POST'])
def addcar():
    error = ""
    form = AddCar()

    if request.method == 'POST':
        newmodel = form.newmodel.data

        if len(newmodel) == 0:
            error = "Please supply model"
        else:
            addnewcar = Cars(model = newmodel)
            db.session.add(addnewcar)
            db.session.commit()
            return 'Car has been added please return to home page'
            #return redirect(url_for('home'))


    return render_template('addcar.html', title='addcar', form=form, message=error)

@app.route('/reviews/<int:id>', methods=['GET', 'POST'])
def reviews(id):
    carryviews = Review.query.filter_by(car_id=id).all()
    error = ""
    form = UpdateReview()

    if request.method == 'POST':
        newreview = form.newreview.data

        if len(newreview) == 0:
            error = "Please fill in review"
        else:
            getcar = Review.query.filter_by(car_id=id).first()
            if not getcar:
                addnewreview = Review(post = newreview, car_id = id)
                db.session.add(addnewreview)
                db.session.commit()
            else:
                getcar.post = newreview
                db.session.commit()
            return 'Review has been updated'
    return render_template('reviews.html', title='review', reviews=carryviews, form=form, message=error)   

@app.route('/delete', methods=['GET', 'DEL'])
def delete():
    carData = Cars.query.all()
    error = ""
    form = DeleteCar()

    return render_template("delete.html", title='Delete', cars=carData, form=form, message=error)

@app.route('/removecar/<int:id>')
def removecar(id):
    getreview = Review.query.filter_by(car_id=id).first()
    if not getreview:
        return "Please attach a review to the car first"
    else:
        carid = getreview.car_id
        cartodelete = Cars.query.filter_by(id=carid).first()
       
        db.session.delete(getreview)
        db.session.commit()
        db.session.delete(cartodelete)
        db.session.commit()
    return 'Car has been deleted, please return to home page'
    

    