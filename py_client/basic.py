import requests


# endpoint = "http://httpbin.org/status/200"

endpoint = "http://httpbin.org/anything"


get_response = requests.get(endpoint, json={'query': "Hello World"})  ## HTTP  Requests
# print(get_response.text) ### print raw text response



print(get_response.json())
# HTTP  Requests > HTML
# REST API  HTTP Requests > JSON
# javaScript Object Notation  ~ python dictionary

print(get_response.status_code)