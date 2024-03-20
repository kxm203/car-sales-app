from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from flask_sqlalchemy import sqlalchemy

from config import db

db = SQLAlchemy()
# Models go here!

class FordMustang(db.Model, SerializerMixin):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String)
    year = db.Column(db.Integer)
    color = db.Column(db.String)
    username = db.column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(de.DateTime, onupdate=db.func.now())

    def __repr_(self):
        return f'<Mustang by {self.username}>'


