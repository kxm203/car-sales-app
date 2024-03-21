#!/usr/bin/env python3

# Standard library imports
from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
from flask_migrate import Migrate 
# Remote library imports
from flask_restful import Resource
# Local imports
from config import app, db, api
# Add your model imports

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app,db)
db.init_app(app)

# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

@app.route('/mustangs', methods=['GET', 'POST'])
def mustangs():
    if request.method == 'GET':
        mustangs = FordMustang.query.order_by('created_at').all()

        response = make_response(
            jsonify([mustang.to_dict() for mustang in mustangs]),
            200,
        )
    elif request.method == 'POST':
        data = request.get_json()
        mustang = FordMustang(
            model=data['model'],
            year=data['year'],
            color=data['color'],
            price=data['price'],
        )
        db.session.add(mustang)
        db.session.commit()

        response = make_response(
            jsonify(message.to_dict()),
            201,
        )
    return response

@app.route('/mustangs/<int:id>', methods=['PATCH', 'DELETE'])
def mustangs_by_id(id):
    mustang = FordMustang.query.filter_by(id=id).first()

    if request.method == 'PATCH':
        data = request.get_json()
        for attr in data:
            setattr(mustang, attr, data[attr])

        db.session.add(mustang)
        db.session.commit()

        response = make_response(
            jsonify(mustang.to_dict()),
            200,
        )

    elif request.method =='DELETE':
        db.session.delete(mustang)
        db.session.commit()

        response = make_reponse(
            jsonify({'deleted': True}),
            200,
        )


if __name__ == '__main__':
    app.run(port=5555, debug=True)

