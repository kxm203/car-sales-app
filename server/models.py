from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
# from flask_sqlalchemy import sqlalchemy

from config import db


# Models go here!

class FordMustang(db.Model, SerializerMixin):
    __tablename__ = 'ford_mustangs'

    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String)
    year = db.Column(db.Integer)
    color = db.Column(db.String)
    bids = db.relationship('Bid', secondary='ford_mustang_bid_association', back_populates='ford_mustangs')
    # username = db.column(db.String)
    # created_at = db.Column(db.DateTime, server_default=db.func.now())
    # updated_at = db.Column(de.DateTime, onupdate=db.func.now())
    def __repr__(self):
        return f'<Mustang by {self.year} {self.color}>'

class Bid(db.Model):
    __tablename__ = 'bids'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='bids')

    def __repr__(self):
        return f'<Bid ${self.amount} by {self.user.username}>'

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    bids = db.relationship('Bid', back_populates='user')

    def __repr__(self):
        return f'<User {self.username}>'

ford_mustang_bid_association = db.Table('ford_mustang_bid_asscoiation',
    db.Column('ford_mustang_id', db.Integer, db.ForeignKey('ford_mustangs.id')),
    db.Column('bid.id', db.Integer, db.ForeignKey('bids.id'))
)     



