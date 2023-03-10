from flaskbs.db import db


class User(db.Model):  # type: ignore [name-defined]
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)
