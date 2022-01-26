import requests
import os
requests.packages.urllib3.disable_warnings()

IP = 'sandboxdnac.cisco.com'
#os.system('ping -c 5 '+IP)
interface = 'GigabitEthernet1'
user = 'devnetuser'
password = 'Cisco123!'
url = f'https://{IP}/restconf/data/ietf-interfaces:interfaces/interface={interface}'
headers = {"Accept":"application/yang-data+json", "Content-type":"applicaton/yang-data+json"}
auth = (user,password)
res = requests.get(url, auth=auth, headers=headers, verify=False)
status_code = res.status_code
print(status_code)
if res.status_code == 200:
    print('Yes - Interface is up - Returning status code: 200')
else:
    print(f'No - Interface is Down - Returning status code: {res.status_code}')