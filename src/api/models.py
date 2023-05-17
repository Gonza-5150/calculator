from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Table, Integer, String, Float, Boolean, Date, Time
from datetime import datetime

db = SQLAlchemy()
Base = declarative_base()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    status = db.Column(db.Boolean, unique=False, nullable=False)
    balance = db.Column(db.Float, default=1000)

    def __repr__(self):
        return f'<User {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "password": self.password,
            "status": self.status,
            "balance": self.balance
        }


class Operation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), unique=False, nullable=False)
    cost = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return f'<Operation {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "type": self.type,
            "cost": self.cost,
        }


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, default=datetime.now().date())

    operation_id = db.Column(db.Integer, db.ForeignKey(
        'operation.id'), nullable=False)
    user_id = operation_id = db.Column(
        db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    user_balance = db.Column(db.Float, nullable=False)
    operation_response = db.Column(db.String(200))

    def serialize(self):
        return {
            "id": self.id,
            "date": self.date,
            "operation_id": self.operation_id,
            "amount": self.amount,
            "user_balance": self.user_balance,
            "user_id": self.user_id,
            "operation_response": self.operation_response

        }
