from uuid import uuid4
from sqlalchemy_utils import UUIDType
from .app import db


def generate_id():
    return uuid4().hex


class Text(db.Model):
    id = db.Column(
        UUIDType(binary=False),
        primary_key=True,
        default=generate_id,
        unique=True,
        nullable=False,
    )
    lines = db.Column(db.Text)
    summary = db.Column(db.Text)
