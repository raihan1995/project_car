from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@34.89.53.51/car_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

db = SQLAlchemy(app)

db.create_all()


