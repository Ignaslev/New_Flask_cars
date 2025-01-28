from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Projektas(db.Model):
    __tablename__ = 'projektas'
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String)
    model = db.Column(db.String)
    year = db.Column(db.Integer)
    price = db.Column(db.Float)
    date = db.Column(db.DateTime, default=datetime.datetime.now)
    image = db.Column(db.String, nullable=True)

    def __repr__(self):
        return f'id: {self.id}; Brand: {self.brand}; Model: {self.price}; price: {self.price}, date: {self.date}'