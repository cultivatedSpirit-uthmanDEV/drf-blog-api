import requests

endpoint = "http://127.0.0.1:8000/api/account/register/"

data = {
    "username" : "baliqis",
    "password" : "baliqis1",
    "email" : "baliqis@gmail.com"
}

get_response = requests.post(endpoint, json=data)

print(get_response)
#print(get_response.text)

print(get_response.status_code)