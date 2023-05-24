import requests


# endpoint = "http://httpbin.org/status/200"

endpoint = "http://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/"


get_response = requests.post(endpoint, json={'title': "ABC 123","content": "Hello World", 'price': "abc123"})  ## HTTP  Requests
# print(get_response.text) ### print raw text response



# print(get_response.json())
# HTTP  Requests > HTML
# REST API  HTTP Requests > JSON
# javaScript Object Notation  ~ python dictionary

# print(get_response.status_code)


# print(get_response.text)
# print(get_response.status_code)
# print(get_response.json()["message"])

print(get_response.json())