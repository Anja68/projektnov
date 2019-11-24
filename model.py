import sqla_wrapper
import os


db = sqla_wrapper.SQLAlchemy(os.getenv("DATABASE_URL", "sqlite:///localhost.sqlite"))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)


class Receipe:
    def __init__(self, name, description, taste):
        self.name =name
        self.description = description
        self.taste = taste