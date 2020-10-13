import requests
import json
LIST_VIEW_ENDPOINT = 'http://127.0.0.1:5000/texts/'

with open('test_payload.json', 'r') as file:
    payloads = json.loads(file.read())

for payload in payloads:
    response = requests.post(LIST_VIEW_ENDPOINT, json=payload)
    print(response.text)