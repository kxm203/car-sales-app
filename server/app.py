#!/usr/bin/env python3

# Standard library imports
from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
from flask_migrate import Migrate 
# Remote library imports
# from flask_restful import Resource
# Local imports
from config import app, db
#api
from models import Mustang, Bid, User
# Add your model imports




# Views go here!



@app.route('/users', methods=['GET', 'POST'])
def all_users():
    users = User.query.all()
    users_list = [user.to_dict() for user in users]
    return make_response(users_list)
   
    # if request.method == 'GET':
    #   response = make_response(
    #         jsonif),
    #         200,
        )
    elif request.method == 'POST':
        data = request.get_json()
        mustang = Mustang(
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

@app.route('/users/<int:id>', methods=['PATCH', 'DELETE'])
def user_by_id(id):
    user = User.query.get(id)
    # user = User.query.filter_by(id=id).first()
    
    if request.method == 'PATCH':
        params = request.json
        for attr in params:
            setattr(user, attr, params[attr])

        db.session.add(user)
        db.session.commit()

        return make_response(user.to_dic())

    elif request.method =='DELETE':
        db.session.delete(user)
        db.session.commit()

        return make_reponse( ' ', 204) 


# if __name__ == '__main__':
#     app.run(port=5555, debug=True)

