import requests
from getpass import getpass

endpoint = "http://127.0.0.1:8000/api/token/"

password = getpass()

get_response = requests.post(endpoint, json={
    "username": "Ernest" , "password" : password
})

print(get_response)
print(get_response.text)

print(get_response.status_code)