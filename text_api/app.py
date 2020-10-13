from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
marshmallow = Marshmallow()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_ECHO'] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///text.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from .models import db
    db.init_app(app)

    from .schemas import marshmallow
    marshmallow.init_app(app)

    from .views import TextAPI
    text_view = TextAPI.as_view('text_api')
    app.add_url_rule('/texts/', defaults={'text_id': None},
                     view_func=text_view, methods=['GET', ])
    app.add_url_rule('/users/', view_func=text_view, methods=['POST', ])
    app.add_url_rule('/users/<int:text_id>', view_func=text_view,
                     methods=['GET', 'PUT', 'DELETE'])
    return app
