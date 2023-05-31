import requests
endpoint = "http://127.0.0.1:8000/api/products/1123232/"

get_response = requests.get(endpoint)  ## HTTP  Requests
print(get_response.json())
