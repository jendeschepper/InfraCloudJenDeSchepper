#! /bin/bash
IP_HOST=sandboxdnac.cisco.com
#ping -c 5 $IP_HOST
INTERFACE=GigabitEthernet1
USERNAME=devnetuser
PASSWORD=Cisco123!
status_code=$(curl -ks -w "%{http_code}" -o /dev/null -u "$USERNAME:$PASSWORD" -H"Accept: application/yang-data+json" "https://$IP_HOST/restconfig/data/ietf-interfaces:interfaces/interface=$INTERFACE")

echo $status_code

if [ $status_code -eq 200 ]
then
    echo "Yes - interface is up - returning status  code: 200"
else
    echo "No -interface is down - returning status code: $status_code"
fi