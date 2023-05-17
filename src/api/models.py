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

    def __repr__(self):
        return f'<Operation {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "date": self.date,
            "op_type": self.op_type,
        }


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, unique=False, nullable=False)
    operation = db.Column(db.String(255), unique=False, nullable=False)
    result = db.Column(db.String(255), unique=False, nullable=False)
    amount = db.Column(db.String(250), unique=False, nullable=True)
    user_balance = db.Column(db.String(250), unique=False, nullable=True)

    user_id = db.Column(db.Integer, ForeignKey(
        'user.id'))

    def __repr__(self):
        return f'<Record {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "date": self.date,
            "operation": self.operation,
            "result": self.result,
            "amount": self.amount,
            "user_balance": self.user_balance,
            "user_id": self.user_id

        }
