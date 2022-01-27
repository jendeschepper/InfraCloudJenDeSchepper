from textwrap import indent
import requests
import json
requests.packages.urllib3.disable_warnings()

#elementen in de curl script
#-i = include http response header
#-k = skip verification
#-X = request method = "OPTIONS"
#-H = extra header to add to the http request = "Accept: application/yang-data+json"
#-u = username and Password

IP_HOST = "192.168.0.234"
Username = "cisco"
Password = "cisco123!"
URL = f'https://{IP_HOST}:443/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity'
HEADER = {'Accept':'application/yang-data+json'}
basicauth = (Username, Password)

result = requests.options(URL, auth=basicauth, headers=HEADER, verify=False)
print(json.dumps(dict(result.headers), indent=2))