import XXXXAXXXXX 
import json
requests.packages.urllib3.XXXXBXXXXX 
DNAC_user = input("Username? ") 
DNAC_psw = input("Password? ")  
token_req_url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"
auth = (DNAC_user, DNAC_psw)
req = requests.post(token_req_url, auth=XXXXCXXXXX, verify=False)
print("API Return Code: " + str(req.status_code))  
print('Request URI: ' + token_req_url)
print("Username: " + DNAC_user)
resp = req.text
token = req.json()[XXXXDXXXXX]
print("Received Token:")
print(token)
print("Length Token:")
print(len(XXXXEXXXXX))