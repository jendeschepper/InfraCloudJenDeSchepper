import requests
import json
import os


IP_HOST = "10.0.2.15"
Username = "cisco"
Password = "cisco123!"
URL = 'https://{IP_Host}:443/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity'
HEADER = {'Accept':'application/yang-data+json'}
AUTH = {Username, Password}
#-i = include http response header
#-k = skip verification
#-X = request method = "OPTIONS"
#-H = extra header to add to the http request = "Accept: application/yang-data+json"
#-u = username and Password

result = requests.request('OPTIONS', URL, auth=AUTH, headers=HEADER, verify=False)
print(result)