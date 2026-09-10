import requests

BASE_URL = 'http://127.0.0.1:8000'

# 1. Login
login_url = f'{BASE_URL}/api/token/'

data1 = {  "username" : "fodilat",
    "password" : "dogxx",
    "email" : "fodilat@gmail.com"}

response = requests.post(login_url, json=data1)

tokens = response.json()

access_token = tokens['access']
refresh_token = tokens['refresh']


# 2. Make API request
headers = {
    'Authorization': f'Bearer {access_token}'
}

response = requests.post(
    f'{BASE_URL}/blogAPI/',
    headers=headers
)


# 3. If access token expired
if response.status_code == 401:

    refresh_response = requests.post(
        f'{BASE_URL}/api/token/refresh/',
        json={
            'refresh': refresh_token
        }
    )

    # 4. Get new access token
    if refresh_response.status_code == 200:

        access_token = refresh_response.json()['access']

        # 5. Retry request
        headers = {
            'Authorization': f'Bearer {access_token}'
        }

        response = requests.get(
            f'{BASE_URL}/blogAPI/',
            headers=headers
        )

print(response.status_code)
print(response.json())