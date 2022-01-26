from email.header import Header
from telnetlib import AUTHENTICATION
import requests
import os
requests.packages.urllib3.disable_warnings()

IP = '192.168.0.234'
os.system('ping -c 5'+IP)
INTERFACE = 'GigabitEthernet1'
USER = 'cisco'
PASSWORD = 'cisco123!'
URL = 'https://'+IP+'/restconf/data/ietf-interfaces:interfaces/interface='+INTERFACE
HEADER = {"Accept":"application/yang-data+json","Content-type":"applicaton/yang-data+json"}
AUTH = {USER,PASSWORD}
status = requests.get(URL, auth= AUTH, headers=HEADER, verify=False)
status_code =str(status.status_code)
print(status_code)
if status.status_code == 200:
    print('Yes - Interface is up - Returing status code: '+status_code)
else:
    print('No - Interface is Down - Returing status code: '+status_code)