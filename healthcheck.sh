#!/bin/bash

echo "==server health check=="
echo "date: $(date)"
echo "USER: $(whoami)"
echo ""


echo "apna naam batao"
read username


echo "konsa website check karein? (jaise google.com):"
read website

echo ""
echo "== $website chek ho rahi hai..=="

ping -c 3 $website

if [  $? -eq  0  ]; then
   echo "$website✔️"
else 
   echo "$website offline hai!❌"
fi

echo ""
echo "==memory usage=="
free -h

echo ""
echo "==report save ho rahi hai..=="
echo "Date: $(date) | User: $username | Website: $website" >> healthcheck_log.txt
echo "report save ho gayi! ✔️"

echo ""
echo"==health check complete!=="

