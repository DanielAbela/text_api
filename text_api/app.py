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
    app.add_url_rule('/texts/', view_func=TextAPI.as_view('show_texts'))
    return app
