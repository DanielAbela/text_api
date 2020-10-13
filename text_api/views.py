from flask import jsonify, request
from flask.views import MethodView

from .summary import Summary
from .models import Text, db
from .schemas import TextSchema


class TextAPI(MethodView):

    def get(self, text_id):
        if not text_id:
            texts = Text.query.order_by(Text.id).all()
            text_schema = TextSchema(many=True)
            return jsonify(text_schema.dump(texts))
        text = Text.query.get(text_id)
        text_schema = TextSchema()
        return text_schema.dump(text)

    def post(self):
        text = request.get_json()
        text['summary'] = Summary(text).create()
        text_schema = TextSchema()
        new_text = text_schema.load(text, session=db.session)
        db.session.add(new_text)
        db.session.commit()
        return text_schema.dump(new_text), 201

    def delete(self, text_id):
        text_to_delete = Text.query.get(text_id)
        db.session.delete(text_to_delete)
        db.session.commit()
        return "Record deleted", 204
