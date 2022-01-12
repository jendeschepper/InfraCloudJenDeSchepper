#! /bin/bash
IP_HOST="192.168.0.234"
ping -c 5 $IP_HOST 
INTERFACE=GigabitEthernet1
USERNAME=cisco
PASSWORD="cisco123!"
status_code=$(curl -ks \
-w "%{XXXXCXXXXX}" \
-o /dev/null \
-u "$USERNAME:$PASSWORD" \
-H "Accept: XXXXDXXXXX" \
"https://$IP_HOST/restconf/data/ietf-interfaces:interfaces/interface=XXXXEXXXXX ")

echo $status_code
if [ $status_code -eq XXXXFXXXXX] ; then 
   echo "Yes - interface is up - returning status code: 200"
else
   echo "No - interface is down - returning status code: $status_code"
XXXXGXXXXX