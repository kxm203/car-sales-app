# Standard library imports
from random import randint, choice as rc

# Remote library imports


# Local imports
from app import app
from config import db
from models import Mustang, Bid, User

# Create a function to seed the database
def seed_database():
    # Use app.app_context() to work within the Flask application context
    with app.app_context():

        # Create instances of FordMustang
        m1 = Mustang(year=1993, color='Red')
        m2 = Mustang(year=2000, color='Blue')

        # Create instances of User
        u1 = User( username ='user1@example.com' )
        u2 = User( username ='user2@example.com' )

        # Create instances of Bid
        b1 = Bid(bid_amount=40000.00, user_name=u1)
        b2 = Bid(bid_amount=36000.00, user_name=u2)

        # Add instances to the database session
        db.session.add(m1)
        db.session.add(m2)
        db.session.add(u1)
        db.session.add(u2)
        db.session.add(b1)
        db.session.add(b2)

        # Commit the changes to the database
        db.session.commit()

if __name__=='__main__':
    seed_database()