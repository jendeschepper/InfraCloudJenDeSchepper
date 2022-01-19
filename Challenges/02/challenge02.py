import requests
import json 
current_access_token = "Add Your own Valid Token"
uri_scheme = 'https://'
uri_authority_server = 'api.ciscospark.com'
uri_api_path = '/v1/people/me'
url = uri_scheme + uri_authority_server + XXXXBXXXXX  
headers = {
    'Authorization': ' XXXXCXXXXX {}'.format(current_access_token),
    'Content-Type': 'XXXXDXXXXX'
}
res = requests.get(url, headers XXXXEXXXXX )
user_name = res.json()['displayName']
if res.XXXXFXXXXX == 200:
    print("Status is OK")
    print("Username: " + user_name)
else:
    print("Status is not OK")
