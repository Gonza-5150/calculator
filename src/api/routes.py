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
            return jsonify(access_token=access_token)
    if (userIn == False):
        return jsonify({"msg": "Correo o contraseña incorrectos"}), 401


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

# ***********************ENPOINT USUARIOS************************
# ---------------------------------------------------------------

# lista todos los médicos


@api.route('/users', methods=["GET"])
def get_usuarios():
    usuarios = User.query.filter().all()
    result = list(map(lambda usuarios: usuarios.serialize(), usuarios))
    response_body = {"usuario": result, "msg": "todos los usuarios"}
    return jsonify(response_body), 200


# ***********************ENPOINT CLIENTES************************
# ---------------------------------------------------------------


# lista por cada cliente


@api.route('/clientes/<int:id_cliente>', methods=["GET"])
def get_cliente(id_cliente):
    cliente = User.query.get(id_cliente)
    return jsonify(user.serialize()), 200

# ____Agregar clientes___


@api.route('/clientes', methods=["POST"])
def add_cliente():
    nombre = request.json.get("nombre", None)
    telefono = request.json.get("telefono", None)
    user_id = request.json.get("user_id", None)

    if nombre is None:
        return jsonify({"msg": "Bad request"}), 400

    if user_id is None:
        return jsonify({"msg": "Bad request"}), 400

    cliente = Cliente(nombre=nombre, telefono=telefono,
                      direccion=direccion, user_id=user_id)
    db.session.add(cliente)
    db.session.commit()

    mascota = Mascota(nombre=nombre_mascota, especie=especie,
                      raza=raza, internamiento=internamiento, cliente_id=cliente.id)
    db.session.add(mascota)
    db.session.commit()

    return jsonify("msg: Datos del cliente añadidos"), 200


# Delete cliente
@api.route('/clientes/<int:id_cliente>', methods=["DELETE"])
def delete_cliente(id_cliente):
    delete = Cliente.query.filter_by(id=id_cliente).first()
    db.session.delete(delete)
    db.session.commit()
    return jsonify({"msj": "Cliente borrado"}), 200

# Put Cliente


@api.route('/clientes/<int:id>', methods=["PUT"])
def update_cliente(id):
    body = request.get_json()
    print(id)
    cliente = Cliente.query.filter(Cliente.id == id).update({
        Cliente.nombre: body["nombre"],
        Cliente.direccion: body["direccion"],
        Cliente.telefono: body["telefono"],
        Cliente.user_id: body["user_id"]}, synchronize_session=False)
    db.session.commit()
    return jsonify({"msj": "Cliente actualizado"}), 200
