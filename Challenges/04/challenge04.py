import requests 
import json
requests.packages.urllib3.disable_warnings() 
DNAC_user = input("Username? ") 
DNAC_psw = input("Password? ")  
token_req_url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"
auth = (DNAC_user, DNAC_psw)
req = requests.post(token_req_url, auth=auth, verify=False)
print(req.headers)
print("API Return Code: " + str(req.status_code))  
print('Request URI: ' + token_req_url)
print("Username: " + DNAC_user)
resp = req.text
token = req.json()['']
print("Received Token:")
print(token)
print("Length Token:")
print(len(token))