import requests
import json 
current_access_token = "NjgxNjQ4NGQtZTM0Yi00MGEzLThiYTUtOWE5OTgyODllMjJjYTgzM2ZlOTUtMWI3_PE93_ca1cc44d-8847-4e5d-83d7-60b457809daa"
uri_scheme = 'https://'
uri_authority_server = 'api.ciscospark.com'
uri_api_path = '/v1/people/me'
url = uri_scheme + uri_authority_server + uri_api_path  
headers = {
    'Authorization': ' bearer {}'.format(current_access_token),
    'Content-Type': 'application/json'
}
res = requests.get(url, headers=headers)

if res.status_code == 200:
    user_name = res.json()['displayName']
    print("Status is OK")
    print("Username: " + user_name)
else:
    print("Status is not OK")
