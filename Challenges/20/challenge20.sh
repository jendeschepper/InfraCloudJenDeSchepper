#!/bin/bash
echo "START DEVICE IOS VERSION  CHECK"
REQUIRED_IOS="16.09.05"
VERSION_SEARCH_TEXT="Cisco IOS XE Software, Version"
echo REQUIRED IOS: $REQUIRED_IOS

echo $(date +"%F")
echo $(date +"%T")
echo 
for f in device_versions/* 
do 
  echo "BEGIN -- Processing file $f" 
  cat $f | grep uptime  | cut -d' ' -f1 
  IOS_VERSION=$(cat $f | grep "$VERSION_SEARCH_TEXT" | cut -d' ' -f6)
  echo Current IOS Version: $IOS_VERSION
  if [ $REQUIRED_IOS != $IOS_VERSION ] 
  then
    echo TO DO: Upgrade IOS version to: $REQUIRED_IOS
  else 
    echo OK: No Upgrade needed
  fi
    echo "END -- Processing file $f"
  echo 
done
echo "END DEVICE IOS VERSION CHECK"
