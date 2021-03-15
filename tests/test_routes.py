import pytest
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask import url_for
from flask_testing import TestCase
from application import app, db, routes
from application.models import Cars, Review, UpdateReview, AddCar, DeleteCar


class TestBase(TestCase):
    def create_app(self):

        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):

        # Create table
        db.create_all()

        # Create test data
        sample1 = Cars(model="tesla")
        sample2 = Review(post="nicecar", car_id=1)

        # Save car to Cars database
        db.session.add(sample1)
        db.session.commit()
        # Save Review to Review database
        db.session.add(sample2)
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):

    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'tesla', response.data)

    def test_about_get(self):
        response = self.client.get(url_for('about'))
        self.assertEqual(response.status_code, 200)
    
    def test_delete_get(self):
        response = self.client.get(url_for('delete'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'tesla', response.data)

    # def test_reviews_get(self):
    #     response = self.client.get(url_for('reviews'))
    #     self.assertEqual(response.status_code, 200)

class TestAdd(TestBase):
    def test_addcar_post(self):
        response = self.client.post(
            url_for('addcar'),
            data = dict(newmodel="mazda"),
            follow_redirects=True
        )
        self.assertIn(b'Car has been added please return to home page',response.data)
        #Test to see when data is queried at home page to see if the car exists
        response1 = self.client.get(url_for('home'))
        self.assertIn(b'mazda',response1.data)
    
    def test_addreview_post(self):
        response = self.client.post(
            url_for('reviews', id=1),
            data = dict(newreview="nicecar"),
            follow_redirects=True
        )

        self.assertIn(b'Review has been updated',response.data)

class TestDelete(TestBase):
    def test_deletecar_del(self):
        response = self.client.get(
            url_for('removecar', id=1),
            data = dict(deletemodel="mazda"),
            follow_redirects=True
        )
        self.assertIn(b'Car has been deleted, please return to home page',response.data)