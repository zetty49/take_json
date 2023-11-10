import requests
import json

with open('product_test.json', 'r') as file:
    json_data = json.load(file)

url = 'http://127.0.0.1:8000/add_data/'

response = requests.post(url, json=json_data)

print(response.status_code)
print(response.text)