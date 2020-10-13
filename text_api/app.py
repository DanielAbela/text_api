from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from settings.common import configure_logging
from settings.local.dev import Config

db = SQLAlchemy()
marshmallow = Marshmallow()

configure_logging()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

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
