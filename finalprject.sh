#!/bin/bash

echo "apna naam batao"
read username


echo "==system report=="
echo "user: $(whoami)"
echo "date: $(date)"
echo "disk usage:"
df -h /

if [ -d "backup"]; then
   echo "backup folder pehle se hai!"
else 
   echo "backup folder nahi hai- bana rahe hai.."
   mkdir backup
fi

tar -czvf backup/backup_$(date +%y%m%d).tar.gz *.txt

for file in backup/*.tar.gz
do 
   echo "$username,yeh backup ban gaya: $file"
done

echo "==script complete!=="

