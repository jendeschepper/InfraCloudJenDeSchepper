import requests
import json
import os


IP_HOST = "192.168.0.234"
Username = "cisco"
Password = "cisco123!"
URL = f'https://{IP_HOST}:443/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity'
HEADER = {'Accept':'application/yang-data+json'}
basicauth = {Username, Password}
#-i = include http response header
#-k = skip verification
#-X = request method = "OPTIONS"
#-H = extra header to add to the http request = "Accept: application/yang-data+json"
#-u = username and Password

result = requests.options(URL, auth=basicauth, headers=HEADER, verify=False)
print(result)