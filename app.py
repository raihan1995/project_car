from application import app, db, routes
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request
from flask import render_template, redirect, url_for, request
from application.models import Cars, Review


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')