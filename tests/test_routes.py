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

        # save car to database
        db.session.add(sample1)
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

# class TestAdd(TestBase):
#     def test_add_car(self):
#         response = self.client.post(
#             url_for('addcar'),
#             data = dict(name="mazda"),
#             follow_redirects=True
#         )
#         self.assertIn(b'mazda',response.data)