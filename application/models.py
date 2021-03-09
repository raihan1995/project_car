from application import app, db

class Cars(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(30), nullable=False)
    reviews = db.relationship('Review', backref='car')

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.String(500), nullable=False)
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'), nullable=False)

#db.drop_all()
db.create_all()

# testuser = Users(first_name='test',last_name='dummy', email= 'tdummy@gmail.com')
# db.session.add(testuser)
# db.session.commit()

# testgame = Games(title='valheim',price='15')
# db.session.add(testgame)
# db.session.commit()

# testorder = Orders(fk_user_id = 3,fk_game_id = 2,order_status = 'Dispatched', order_created = '2021-03-04 16-00-00' )
# db.session.add(testorder)
# db.session.commit()

# db.drop_all()
# db.create_all()