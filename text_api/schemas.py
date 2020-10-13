from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from .models import Text

marshmallow = Marshmallow()


class TextSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Text
        include_relationships = True
        load_instance = True

