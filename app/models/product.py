from app.db import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.String(120))

    def __init__(self, price):
        self.price = price

    def update_price(self, new_price):
        self.price = new_price
