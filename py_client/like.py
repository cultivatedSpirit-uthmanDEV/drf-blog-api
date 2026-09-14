import requests

BASE_URL = "http://127.0.0.1:8000"

login_endpoint = f"{BASE_URL}/api/token/"
like_endpoint = f"{BASE_URL}/blogAPI/post/4/like/"

data = {
    "username": "fodilat",
    "password": "dogxx"
}

# Login
response = requests.post(login_endpoint, json=data)

print("Login:", response.status_code)

tokens = response.json()
access_token = tokens["access"]

headers = {
    "Authorization": f"Bearer {access_token}"
}

# Like the post
response = requests.post(like_endpoint, headers=headers)

print("Like:", response.status_code)
print(response.json())