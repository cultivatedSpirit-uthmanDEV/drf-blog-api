import requests

BASE_URL = "http://127.0.0.1:8000"
endpoint = f"{BASE_URL}/blogAPI/post/4/create/comment/"
login_endpoint = "http://127.0.0.1:8000/api/token/"




data = {  "username" : "fodilat",
    "password" : "dogxx",
    "email" : "fodilat@gmail.com"}

get_response = requests.post(login_endpoint, json=data)

print(get_response.status_code)
# print(get_response.text)

tokens = get_response.json()
access_token = tokens['access']





if get_response.status_code == 200:

    headers = {
        'Authorization' : f"Bearer {access_token}"
    }
    data1 = {
        'content' : 'This is a new comment'
    }



    get_response = requests.post(endpoint, json=data1, headers=headers)

    print(get_response.status_code)
    print(get_response.json())

if get_response.status_code == 401:
        refresh_token = tokens['refresh']

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
            
            data = {
                
                'content' : 'This is a new comment'
            }
        
            get_response = requests.post(endpoint, json=data, headers=headers)
            

            

            print(get_response.status_code)
            print(get_response.json())


