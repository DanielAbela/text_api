from uuid import uuid4

from .app import db


def generate_id():
    return uuid4().hex



class Text(db.Model):
    id = db.Column(db.Integer, primary_key=True, default=generate_id)
    lines = db.Column(db.Text)
    summary = db.Column(db.Text)
