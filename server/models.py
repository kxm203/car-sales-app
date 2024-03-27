from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates
# from faker import Faker
from config import db


# Models go here!
# fake = Faker()
class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    serialize_rules = ('-bids.user',)

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(2), unique=True, nullable=False)
    age = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    # def __repr__(self):
    #     return f'<User {self.username}>'
    bids = db.relationship('Bid', back_populates='user')
    bids_mustangs = association_proxy('bids', 'mustang')

    __table_args__ = (
        db.CheckConstraint('age > 21'),
    )

    @validates('username')
    def validate_username(self, key, new_username):
        if len(new_username) <= 2:
            raise ValueError('Username must be greater than 2 characters')
        return new_username
    

class Mustang(db.Model, SerializerMixin):
    __tablename__ = 'mustangs'

    serialize_rules = ('-bids.mustang',)

    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    color = db.Column(db.String)
    price = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    bids = db.relationship('Bid', back_populates='mustang', cascade='all, delete-orphan')
    users = association_proxy('bids,', 'user')

    # bids = db.relationship('Bid', secondary='mustang_bid', back_populates='mustangs')
    # username = db.column(db.String)
    # created_at = db.Column(db.DateTime, server_default=db.func.now())
    # updated_at = db.Column(de.DateTime, onupdate=db.func.now())
    # def __repr__(self):
    #     return f'<Mustang by {self.year} {self.color}>'


class Bid(db.Model, SerializerMixin):
    __tablename__ = 'bids'

    serialize_rules = ('-mustang.bids', '-user.bids')

    id = db.Column(db.Integer, primary_key=True)
    bid_amount = db.Column(db.Integer, unique=True, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @property
    def validate_bid_amount(self, key, bid_amount):
        if self.bid_amount < 1000 or self.bid_amount > 500000:
            raise ValueError('Bid amount must be between 1000 and 500000.')
        return bid_amount
    
    mustang_id = db.Column(db.Integer, db.ForeignKey('mustangs.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
   
    # def __repr__(self):
    #     return f'<Bid ${self.amount} by {self.user.username}>'

    mustang = db.relationship('Mustang', back_populates='bids')
    user = db.relationship('User', back_populates='bids')

 

