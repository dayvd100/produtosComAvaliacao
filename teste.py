import requests

response = requests.get("http://127.0.0.1:8000/")

data_json = response.json()

print(data_json)
