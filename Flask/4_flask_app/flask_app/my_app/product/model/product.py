from my_app import db

class Product(db.Model):
    __tablename__= 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    price = db.Column(db.Float)
   
    def __init__(self, name, price):
            self.name = name
            self.price = price

    def __repr__(self):
        return '<Product %r>' % (self.name)