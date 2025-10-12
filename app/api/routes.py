from flask import jsonify, request
from . import bp
from app import mongo


@bp.route('/users', methods=['POST'])
def add_user():
    users_collection = mongo.db.users
    user_data = request.json

    result = users_collection.insert_one(user_data)

    return jsonify({"message":"user added successfully", "id":str(result.inserted_id)}),201

@bp.route('/users', methods=['GET'])
def get_all_users():
    users_collection = mongo.db.users_collection

    all_users = list(users_collection.find())

    return jsonify(str(all_users))