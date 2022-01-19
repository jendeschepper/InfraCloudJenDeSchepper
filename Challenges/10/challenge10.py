import requests

IP_Host = "192.168.0.234"
Username = "cisco"
Password = "cisco123!"

#-i = include http response header
#-k = skip verification
#-X = request method = "OPTIONS"
#-H = extra header to add to the http request = "Accept: application/yang-data+json"
#-u = username and Password

result = requests.get('https://{IP_Host}:443/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity')