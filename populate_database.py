import json

import requests

LIST_VIEW_ENDPOINT = 'http://127.0.0.1:5000/texts/'

with open('test_payload.json', 'r') as file:
    payloads = json.loads(file.read())

def populate_database():
    for payload in payloads:
        response = requests.post(LIST_VIEW_ENDPOINT, json=payload)
        print(response.text)


def delete_all():
    for number in range(1, 4):
        response = requests.delete(f'{LIST_VIEW_ENDPOINT}/{number}')
        print(response.text)

populate_database()
# delete_all()
