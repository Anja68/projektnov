import sqla_wrapper
import os


#SQLITE_FILE = ':memory:'
SQLITE_FILE = 'localhost.squlite'

db = sqla_wrapper.SQLAlchemy(os.getenv("DATABASE_URL", "sqlite:///{SQLITE_FILE}"))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    session_token = db.Column(db.String, nullable=True)
    session_expiry_datetime = db.Column(db.DateTime, nullable=True)

class Receipe (db.Model):
    id = db.Column (db.Integer, primary_key=True)
    name = db.Column (db.String, unique=True)
    description = db.Column(db.String, unique=True)
    taste = db.Column(db.String, unique=True)

class books (db.Model):
    id = db.Column (db.Integer, primary_key=True)
    title = db.Column (db.String, unique=True)
    bookdescription = db.Column(db.String, unique=True)