import requests

response = requests.get("http://127.0.0.1:8000/produtos")

products_list = response.content

print(type(products_list))
