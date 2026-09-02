import requests

Base_url = 'http://127.0.0.1:8000'
endpoint = (f'{Base_url}/api/token/')

data1 = {  "username" : "fodilat",
    "password" : "dogxx",
    "email" : "fodilat@gmail.com"}

get_response = requests.post(endpoint, json=data1)

print(get_response.status_code)
# print(get_response.text)

tokens = get_response.json()
access_token = tokens['access']

data3 = {
    'title' : 'My first post6',
    'content' : 'Hello bro6'
}
headers = {'Authorization' : f'Bearer {access_token}'}
post_response = requests.post(f'{Base_url}/blogAPI/', json=data3, headers=headers)

print(post_response.json())
print(post_response.status_code)