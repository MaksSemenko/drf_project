import requests

endpoint = "http://localhost:8000/api/products/1242336756/"

get_response = requests.get(endpoint, json={'title': 'Hello world'})
print(get_response.json())