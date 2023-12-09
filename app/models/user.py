import enum
from datetime import datetime

from app.db import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    phone_number = db.Column(db.String(20))
    address = db.Column(db.String(255))
    city = db.Column(db.String(50))
    region = db.Column(db.String(50))
    country = db.Column(db.String(50))
    card_number = db.Column(db.String(20))
    expiration_date = db.Column(db.String(10))
    cvc = db.Column(db.String(4))

    def __init__(
        self,
        name,
        email,
        password,
        phone_number=None,
        address=None,
        city=None,
        region=None,
        country=None,
        card_number=None,
        expiration_date=None,
        cvc=None,
    ):
        self.name = name
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.address = address
        self.city = city
        self.region = region
        self.country = country
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.cvc = cvc

    def to_json(self):
        return {
            "id": self.id,
            "createdAt": self.created_at.isoformat() if self.created_at else None,
            "name": self.name,
            "email": self.email,
            "phoneNumber": self.phone_number,
            "address": self.address,
            "city": self.city,
            "region": self.region,
            "country": self.country,
            "cardNumber": self.card_number,
            "expirationDate": self.expiration_date,
            "cvc": self.cvc,
        }
