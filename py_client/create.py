import requests

headers={'Authorization': 'Bearer 87702adb12c6754dbba6fdc3ebf7d5451666b4a7'}
endpoint = "http://127.0.0.1:8000/api/products/"

data = {
    'title':'pakistan zindabad   786',
    "price": 32.99,
}
get_response = requests.post(endpoint, json=data, headers=headers)  ## HTTP  Requests
print(get_response.json())