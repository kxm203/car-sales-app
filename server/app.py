#!/usr/bin/env python3

# Standard library imports
from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate 
# Remote library imports
# from flask_restful import Resource
# Local imports
from config import app, CORS, db 
#api
from models import Mustang, Bid, User
# Add your model imports




# Views go here!

@app.route('/users', methods=['GET', 'POST'])
def all_users():
    users = User.query.all()
    users_list = [user.to_dict(rules= ('-mustangs')) for user in users]
    if request.method == 'GET':
       
        return make_response(users_list)
   
    
    elif request.method == 'POST':
        data = request.get_json()
        user = User(
            username=data['username'],
        )
        db.session.add(user)
        db.session.commit()

        response = make_response(
            jsonify(user.to_dict()),
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

        return make_response(user.to_dict())

    elif request.method =='DELETE':
        db.session.delete(user)
        db.session.commit()

        return make_response( ' ', 204) 



@app.route('/mustangs', methods=['GET', 'POST'])
def all_mustangs():
    if request.method == 'GET':
        mustangs = Mustang.query.all()
        mustangs_list = [mustang.to_dict() for mustang in mustangs]
        return make_response(mustangs_list)
   
    
    if request.method == 'POST':
        data = request.get_json()
        # Create a new Mustang
        mustang = Mustang(
            year=data['year'],
            color=data['color'],
            price=data['price'],
            image_url = data.get('image_url')
        )
        db.session.add(mustang)
        db.session.commit()


        response = make_response(
            jsonify(mustang.to_dict()),
            201,
        )
    return response

@app.route('/mustangs/<int:id>', methods=['PATCH', 'DELETE'])
def mustang_by_id(id):
    mustang = Mustang.query.get(id)
    
    if request.method == 'PATCH':
        params = request.json
        for attr in params:
            setattr(mustang, attr, params[attr])

        db.session.add(mustang)
        db.session.commit()

        return make_response(mustang.to_dict())

    elif request.method =='DELETE':
        db.session.delete(mustang)
        db.session.commit()

        return make_response("Mustang was deleted.", 204) 

@app.route('/bids', methods=['GET', 'POST'])
def all_bids():
    if request.method == 'GET':
        bids = Bid.query.all()
        bids_list = [bid.to_dict() for bid in bids]
        return make_response(bids_list)
   
    
    if request.method == 'POST':
        data = request.get_json()
        # Create a new bid
        try:
            bid = Bid(
                # username=data['username'],
                bid_amount=data['bid_amount'],
                user_id=1,
                mustang_id=data['mustang_id'],
            )
            db.session.add(bid)
            db.session.commit()


            response = make_response(
                jsonify(bid.to_dict()),
                201,
            )
        except ValueError as e:
            db.session.rollback()

            response = make_response(
                jsonify(message=str(e)),
                400,
            )
    return response

@app.route('/bids/<int:id>', methods=['PATCH', 'DELETE'])
def bid_by_id(id):
    bid = Bid.query.get(id)
    
    if request.method == 'PATCH':
        params = request.json
        for attr in params:
            setattr(bid, attr, params[attr])

        db.session.add(bid)
        db.session.commit()

        return make_response(bid.to_dict())

    elif request.method =='DELETE':
        db.session.delete(bid)
        db.session.commit()

        return make_response("message:" "Bid was deleted.", 204) 


if __name__ == '__main__':
    app.run(port=5555, debug=True)

