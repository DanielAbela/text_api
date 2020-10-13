import json

import requests

from page_scraper import scrape_url

LIST_VIEW_ENDPOINT = 'http://127.0.0.1:5000/texts/'
URLS = [
    'https://squirro.com/2020/05/29/how_synpulse_is_using_squirro_over_aws_to_provide_fs_firms_with_a_competitive_edge/'
]

for url in URLS:
    payload = dict(lines=scrape_url(url))
    response = requests.post(LIST_VIEW_ENDPOINT, json=payload)
    print(response.text)
