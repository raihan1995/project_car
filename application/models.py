from application import app, db

class Cars(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(30), nullable=False)
    reviews = db.relationship('Review', backref='car')



class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.String(500), nullable=False)
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'), nullable=False)

# db.drop_all()
# db.create_all()

# testcar = Cars(model='bmw')
# db.session.add(testcar)
# db.session.commit()

# testreview = Review(post='test bmw', car_id= 1)
# db.session.add(testreview)
# db.session.commit()

# testcar = Cars(model='mercedes')
# db.session.add(testcar)
# db.session.commit()

# testreview = Review(post='test mercedes', car_id= 2)
# db.session.add(testreview)
# db.session.commit()