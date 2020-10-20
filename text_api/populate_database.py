import os

import requests

from utils import scrape_url
from .app import db, create_app

LIST_VIEW_ENDPOINT = "http://127.0.0.1:5000/texts/"
URLS = [
    "https://en.wikipedia.org/wiki/J._M._W._Turner",
    "https://en.wikipedia.org/wiki/Johann_Sebastian_Bach",
    "https://en.wikipedia.org/wiki/Wolfgang_Amadeus_Mozart",
    "https://en.wikipedia.org/wiki/Sergei_Rachmaninoff",
    "https://en.wikipedia.org/wiki/B%C3%A9la_Bart%C3%B3k",
]

if os.path.exists("text.db"):
    os.remove("text.db")

app = create_app()
app.app_context().push()
db.create_all()


def populate_database():
    for url in URLS:
        payload = dict(lines=scrape_url(url))
        app.logger.info("Making request to %s with payload %s:", url, payload)
        response = requests.post(LIST_VIEW_ENDPOINT, json=payload)
        app.logger.info("Response: %s", response.text)


populate_database()
