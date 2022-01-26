import imp
import json
import requests
import os
from requests.models import Response
requests.packages.urllib3.disable_warnings()
os.environ['User']='cisco'
os.environ['Pass']='cisco123!'

api_url = "https://192.168.0.234/restconf/data/ietf-interfaces:interfaces"
basicauth = (os.environ.pop('User'), os.environ.pop('Pass'))
headers = { "Accept": "application/yang-data+json",
            "Content-type": "application/yang-data+json" }

resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)

response_json = resp.json()
print(json.dumps(response_json, indent=4))