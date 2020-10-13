import sys
from logging.config import dictConfig

from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
marshmallow = Marshmallow()


dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
            }
        },
        "handlers": {
            "wsgi": {
                "class": "logging.StreamHandler",
                "stream": sys.stdout,
                "formatter": "default",
            }
        },
        "root": {"level": "INFO", "handlers": ["wsgi"]},
    }
)


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///text.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    from .models import db

    db.init_app(app)

    from .schemas import marshmallow

    marshmallow.init_app(app)

    from .views import TextAPI

    text_view = TextAPI.as_view("text_api")
    app.add_url_rule(
        "/texts/",
        defaults={"text_id": None},
        view_func=text_view,
        methods=[
            "GET",
        ],
    )
    app.add_url_rule(
        "/texts/",
        view_func=text_view,
        methods=[
            "POST",
        ],
    )
    app.add_url_rule(
        "/texts/<string:text_id>", view_func=text_view, methods=["GET", "PUT", "DELETE"]
    )
    return app
