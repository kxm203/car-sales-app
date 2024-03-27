from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
# from flask_sqlalchemy import sqlalchemy
# from faker import Faker
from config import db


# Models go here!
# fake = Faker()
class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    # serialize_rule =

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    
    # email = db.Column(db.String(120), unique=True, nullable=False)
    # password_hash = db.Column(db.String(128), nullable=False)
    # bids = db.relationship('Bid', back_populates='user')

    # def __repr__(self):
    #     return f'<User {self.username}>'


class Bid(db.Model):
    __tablename__ = 'bids'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False )
    bid_amount = db.Column(db.Integer, unique=True, nullable=False)

    @property
    def validate_bid_amount(self, key, bid_amount):
        if self.bid_amount < 1000 or self.bid_amount > 500000:
            raise ValueError('Bid amount must be between 1000 and 500000.')
        return bid_amount
    # start_amount = db.Column(db.Float, nullable=False)
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # user = db.relationship('User', back_populates='bids')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    mustang_id = db.Column(db.Integer, db.ForeignKey('mustangs.id'))
    # def __repr__(self):
    #     return f'<Bid ${self.amount} by {self.user.username}>'

# mustang_bid = db.Table('mustang_bid',
#     db.Column('mustang_id', db.Integer, db.ForeignKey('mustangs.id')),
#     db.Column('bid.id', db.Integer, db.ForeignKey('bids.id'))
# )     

class Mustang(db.Model, SerializerMixin):
    __tablename__ = 'mustangs'

    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    color = db.Column(db.String)
    price = db.Column(db.Integer)

    # bids = db.relationship('Bid', secondary='mustang_bid', back_populates='mustangs')
    # username = db.column(db.String)
    # created_at = db.Column(db.DateTime, server_default=db.func.now())
    # updated_at = db.Column(de.DateTime, onupdate=db.func.now())
    # def __repr__(self):
    #     return f'<Mustang by {self.year} {self.color}>'
