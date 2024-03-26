# Standard library imports
from random import randint, choice as rc

# Remote library imports


# Local imports
from app import app
from config import db
from models import FordMustang, Bid, User

# Create instances of FordMustang
m1 = Mustang(model='Mustang GT', year=1993, color='Red', price=20000.00)
m2 = Mustang(model='Mustang LX', year=2000, color='Blue', price=5000.00)

# Create instances of User
u1 = User( user_name ='user1@example.com' )
u2 = User( user_name ='user2@example.com' )

# Create instances of Bid
b1 = Bid(amount=40000.00, user=u1)
b2 = Bid(amount=36000.00, user=u2)

# Add instances to the database session
db.session.add(m1)
db.session.add(m2)
db.session.add(u1)
db.session.add(u2)
db.session.add(b1)
db.session.add(b2)

# Commit the changes to the database
db.session.commit()