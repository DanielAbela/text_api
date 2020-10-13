from flask_marshmallow import Marshmallow

from .models import Text

marshmallow = Marshmallow()


class TextSchema(marshmallow.SQLAlchemySchema):
    class Meta:
        model = Text

    id = marshmallow.auto_field()
    lines = marshmallow.auto_field()
    summary = marshmallow.auto_field()
