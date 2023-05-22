"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Operation, Record
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
import json
from datetime import datetime
import math
import random

api = Blueprint('api', __name__)


# ___________POST-TOKEN__________
@api.route("/token", methods=["POST"])
def login():
    userIn = False
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    user = User.query.filter().all()
    result = list(map(lambda user: user.serialize(), user))
    for x in result:
        if (email == x["email"]) and (password == x["password"]):
            userIn = True
            access_token = create_access_token(identity=email)
            return jsonify(access_token=access_token, user_id=x["id"])
    if (userIn == False):
        return jsonify({"msg": "Correo o contraseña incorrectos"}), 401


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200


# All Users


@api.route('/users', methods=["GET"])
def get_usuarios():
    usuarios = User.query.filter().all()
    result = list(map(lambda usuarios: usuarios.serialize(), usuarios))
    response_body = {"usuario": result, "msg": "todos los usuarios"}
    return jsonify(response_body), 200


# Each User


@api.route('/users/<int:user_id>', methods=["GET"])
def get_user(user_id):
    user = User.query.get(user_id)
    return jsonify(user.serialize()), 200

# ADDITION **


@api.route('/addition', methods=["POST"])
def addition():
    data = request.json
    user_id = data['user_id']
    amount1 = data['amount1']
    amount2 = data['amount2']

    user = User.query.get(user_id)
    operation = Operation.query.filter_by(type='addition').first()

    if not user or not operation:
        return jsonify({'messaje': 'User or operation not found'}), 404

    cost = operation.cost
    user_balance = user.balance - cost

    if user_balance < 0:
        return jsonify({'message': 'Insuficient balance'}), 403

    result = int(amount1) + int(amount2)
    record = Record(
        operation_id=operation.id,
        user_id=user.id,
        amount=result,
        user_balance=user_balance,
        operation_response=str(result),
        date=datetime.now()
    )

    db.session.add(record)
    db.session.commit()

    return jsonify({'result': result}), 200

# SUBSTRACTION ***


@api.route('/substraction', methods=["POST"])
def substraction():
    data = request.json
    user_id = data['user_id']
    amount1 = data['amount1']
    amount2 = data['amount2']

    user = User.query.get(user_id)
    operation = Operation.query.filter_by(type='substraction').first()

    if not user or not operation:
        return jsonify({'messaje': 'User or operation not found'}), 404

    cost = operation.cost
    user_balance = user.balance - cost

    if user_balance < 0:
        return jsonify({'message': 'Insuficient balance'}), 403

    result = int(amount1) - int(amount2)
    record = Record(
        operation_id=operation.id,
        user_id=user.id,
        amount=result,
        user_balance=user_balance,
        operation_response=str(result),
        date=datetime.now()
    )

    db.session.add(record)
    db.session.commit()

    return jsonify({'result': result}), 200

# DIVISION ***


@api.route('/division', methods=["POST"])
def division():
    data = request.json
    user_id = data['user_id']
    amount1 = data['amount1']
    amount2 = data['amount2']

    user = User.query.get(user_id)
    operation = Operation.query.filter_by(type='division').first()

    if not user or not operation:
        return jsonify({'messaje': 'User or operation not found'}), 404

    cost = operation.cost
    user_balance = user.balance - cost

    if user_balance < 0:
        return jsonify({'message': 'Insuficient balance'}), 403

    result = int(amount1) / int(amount2)
    record = Record(
        operation_id=operation.id,
        user_id=user.id,
        amount=result,
        user_balance=user_balance,
        operation_response=str(result),
        date=datetime.now()
    )

    db.session.add(record)
    db.session.commit()

    return jsonify({'result': result}), 200

# MULTIPLICATION ***


@api.route('/multiplication', methods=["POST"])
def multiplication():
    data = request.json
    user_id = data['user_id']
    amount1 = data['amount1']
    amount2 = data['amount2']

    user = User.query.get(user_id)
    operation = Operation.query.filter_by(type='multiplication').first()

    if not user or not operation:
        return jsonify({'messaje': 'User or operation not found'}), 404

    cost = operation.cost
    user_balance = user.balance - cost

    if user_balance < 0:
        return jsonify({'message': 'Insuficient balance'}), 403

    result = int(amount1) * int(amount2)
    record = Record(
        operation_id=operation.id,
        user_id=user.id,
        amount=result,
        user_balance=user_balance,
        operation_response=str(result),
        date=datetime.now()
    )

    db.session.add(record)
    db.session.commit()

    return jsonify({'result': result}), 200

# SQRT


@api.route('/sqrt', methods=["POST"])
def sqrt():
    data = request.json
    user_id = data['user_id']
    amount1 = data['amount1']

    user = User.query.get(user_id)
    operation = Operation.query.filter_by(type='multiplication').first()

    if not user or not operation:
        return jsonify({'messaje': 'User or operation not found'}), 404

    cost = operation.cost
    user_balance = user.balance - cost

    if user_balance < 0:
        return jsonify({'message': 'Insuficient balance'}), 403

    if amount1 < 0:
        return jsonify({'message': 'Invalid input: number must be not negative'}), 400

    result = math.sqrt(amount1)
    record = Record(
        operation_id=operation.id,
        user_id=user.id,
        amount=result,
        user_balance=user_balance,
        operation_response=str(result),
        date=datetime.now()
    )

    db.session.add(record)
    db.session.commit()

    return jsonify({'result': result}), 200

# RANDOM


@api.route('/randn', methods=["POST"])
def randn():
    data = request.json
    user_id = data['user_id']
    amount1 = data['amount1']
    amount2 = data['amount2']

    user = User.query.get(user_id)
    operation = Operation.query.filter_by(type='randn').first()

    if not user or not operation:
        return jsonify({'message': 'User or operation not found'}), 404

    cost = operation.cost
    user_balance = user.balance - cost

    if user_balance < 0:
        return jsonify({'message': 'Insufficient balance'}), 403

    if amount1 >= amount2:
        return jsonify({'message': 'Invalid input: range_min must be less than range_max'}), 400

    result = random.randint(amount1, amount2)
    record = Record(
        operation_id=operation.id,
        user_id=user.id,
        amount=result,
        user_balance=user_balance,
        operation_response=str(result),
        date=datetime.utcnow().date()
    )

    db.session.add(record)
    db.session.commit()

    return jsonify({'result': result}), 200


# Delete user
# @api.route('/users/<int:id_user>', methods=["DELETE"])
# def delete_user(id_cliente):
#     delete = User.query.filter_by(id=id_user).first()
#     db.session.delete(delete)
#     db.session.commit()
#     return jsonify({"msj": "Bye User!"}), 200
