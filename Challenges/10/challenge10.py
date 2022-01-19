import requests

IP_Host = "10.0.2.15"
Username = "cisco"
Password = "cisco123!"

#-i = include http response header
#-k = skip verification
#-X = request method = "OPTIONS"
#-H = extra header to add to the http request = "Accept: application/yang-data+json"
#-u = username and Password
header = {'Accept':'application/yang-data+json'}
result = requests.request('OPTIONS', 'https://{IP_Host}:443/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity', auth=(Username, Password), headers=header, verify=False)