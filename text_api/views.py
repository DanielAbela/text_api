from flask import jsonify, request, Flask
from flask.views import MethodView

from .models import Text, db
from .schemas import TextSchema
from .summary import Summary

app = Flask(__name__)


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
        app.logger.debug("Creating summary for text: %s", text["lines"])
        text["summary"] = Summary(text["lines"]).create()
        app.logger.debug("Summary created: %s", text["summary"])
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


class SummaryAPI(MethodView):
    def get(self, text_id):
        text = Text.query.get(text_id)
        text_schema = TextSchema()
        text = text_schema.dump(text)
        return jsonify(
            {key: value for key, value in text.items() if key in ["id", "summary"]}
        )
