from email.header import Header
from telnetlib import AUTHENTICATION
import requests
import os
requests.packages.urllib3.disable_warnings()

IP = '192.168.0.234'
os.system('ping -c 5'+IP)
interface = 'GigabitEthernet1'
user = 'cisco'
password = 'cisco123!'
url = 'https://'+IP+'/restconf/data/ietf-interfaces:interfaces/interface='+interface
headers = {"Accept":"application/yang-data+json","Content-type":"applicaton/yang-data+json"}
auth = {user,password}
status = requests.get(url, auth= auth, headers=headers, verify=False)
status_code =str(status.status_code)
print(status_code)
if status.status_code == 200:
    print('Yes - Interface is up - Returing status code: '+status_code)
else:
    print('No - Interface is Down - Returing status code: '+status_code)