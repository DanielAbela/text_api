from flask import jsonify, request
from flask.views import MethodView

from .models import Text, db
from .schemas import TextSchema


class TextAPI(MethodView):

    def get(self):
        texts = Text.query.order_by(Text.id).all()
        text_schema = TextSchema(many=True)
        return jsonify(text_schema.dump(texts))

    def post(self):
        text = request.get_json()
        schema = TextSchema()
        new_text = schema.load(text, session=db.session).data
        db.session.add(new_text)
        db.session.commit()

        return schema.dump(new_text).data, 201