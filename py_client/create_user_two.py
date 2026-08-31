import requests


base_url = 'http://127.0.0.1:8000/'
login_url = f"{base_url}/api/token/"

data = {
    "username" : "baliqis",
    "password" : "baliqis1",
    "email" : "baliqis@gmail.com"
}


get_response = requests.post(login_url, json=data)
token = get_response.json()
access_token = token['access']

headers = {'Authorization' : f'Bearer {access_token}'}

endpoint = f"{base_url}/blogAPI/"

data2 = {
    "title": "implement Api",
    "content" : "i will implement this!!!"
}

get_response = requests.post(endpoint,headers=headers, json=data2)

print(get_response.status_code)
print(get_response.json())

