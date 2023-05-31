import requests
endpoint = "http://127.0.0.1:8000/api/products/5/update/"


data = {
    "title" : "Hello world my old friend ",
    'price' : 129.99
}
get_response = requests.put(endpoint, json=data)  ## HTTP  Requests
print(get_response.json())
