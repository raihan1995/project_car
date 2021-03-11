from application import app, db
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class Cars(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(30), nullable=False)
    reviews = db.relationship('Review', backref='car')

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.String(500), nullable=False)
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'), nullable=False)

class UpdateReview(FlaskForm):
    newreview = StringField('Review', validators=[DataRequired()])
    submit = SubmitField('Update Review')

class AddCar(FlaskForm):
    newmodel = StringField('Model', validators=[DataRequired()])
    submit = SubmitField('Add Car')

class DeleteCar(FlaskForm):
    deletemodel = StringField('Enter car to delete:', validators=[DataRequired()])
    submit = SubmitField('Delete Car')  
    

# db.drop_all()
# db.create_all()

# testcar = Cars(model='bmw')
# db.session.add(testcar)
# db.session.commit()

# testreview = Review(post='test ford', car_id= 3)
# db.session.add(testreview)
# db.session.commit()

# testcar = Cars(model='mercedes')
# db.session.add(testcar)
# db.session.commit()

# testreview = Review(post='test mercedes', car_id= 2)
# db.session.add(testreview)
# db.session.commit()

