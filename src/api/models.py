from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Table, Integer, String, Float, Boolean, Date, Time

db = SQLAlchemy()
Base = declarative_base()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    status = db.Column(db.Boolean, unique=False, nullable=False)
    amount = db.Column(db.String(250), unique=False, nullable=True)

    def __repr__(self):
        return f'<User {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "password": self.password
        }


class Operation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, unique=False, nullable=False)
    op_type = db.Column(db.Date, unique=False, nullable=False)
    user_id = db.Column(db.Integer, ForeignKey(
        'user.id'))
    user = db.relationship('User')

    def __repr__(self):
        return f'<Vacuna {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "date": self.date,
            "op_type": self.op_type,
            "user_id": self.user_id,
            "user": self.user
        }


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, unique=False, nullable=False)
    operation = db.Column(db.String(255), unique=False, nullable=False)
    result = db.Column(db.String(255), unique=False, nullable=False)
    user_id = db.Column(db.Integer, ForeignKey(
        'user.id'))
    user = db.relationship('User')

    def __repr__(self):
        return f'<Record {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "date": self.date,
            "user_id": self.user_id,
            "user": self.user,
            "operation": self.operation,
            "result": self.result
        }
