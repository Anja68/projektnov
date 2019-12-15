import sqla_wrapper
import os


#SQLITE_FILE = ':memory:'
SQLITE_FILE = 'localhost.squlite'


db = sqla_wrapper.SQLAlchemy(os.getenv("DATABASE_URL", "sqlite:///{SQLITE_FILE}"))

db = sqla_wrapper.SQLAlchemy("postgres://lpaxzzahukrfni:77e2683ba871c1f4c5cf35fe88f4fdca666f12382f60cd13cb86040fdc7b8714@ec2-46-137-187-23.eu-west-1.compute.amazonaws.com:5432/d525g6c8fq274d")


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