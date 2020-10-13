import os

import requests
from flask import Flask

from utils import scrape_url
from .app import db, create_app

app = Flask(__name__)

LIST_VIEW_ENDPOINT = "http://127.0.0.1:5000/texts/"
URLS = [
    "https://squirro.com/2020/05/29/how_synpulse_is_using_squirro_over_aws_to_provide_fs_firms_with_a_competitive_edge/",
    # "https://squirro.com/2020/09/25/the-squirro-approach-to-training-and-certification/",
    # "https://squirro.com/2020/05/28/squirro-partners-with-wipro-to-help-customers-become-intelligent-enterprises/",
    # "https://squirro.com/2020/04/24/squirro-launches-transportation-monitoring-application/",
    # "https://squirro.com/2020/03/27/a-letter-to-our-community-of-customer-prospects-and-partners/"
]

if os.path.exists("text.db"):
    os.remove("text.db")

app = create_app()
app.app_context().push()
db.create_all()


def populate_database():
    for url in URLS:
        payload = dict(lines=scrape_url(url))
        app.logging.info('Making request to %s with payload %s:', url, payload)
        response = requests.post(LIST_VIEW_ENDPOINT, json=payload)
        app.logging.info('Response: %s', response.text)
