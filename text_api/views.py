from flask import jsonify
from flask.views import View

from .models import Text
from .schemas import TextSchema


class ShowTexts(View):

    def dispatch_request(self):
        texts = Text.query.order_by(Text.id).all()
        text_schema = TextSchema(many=True)
        return jsonify(text_schema.dump(texts))

