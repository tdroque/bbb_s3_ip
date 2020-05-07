#!/bin/bash
PASSWORD = " " #ssh password

python3 ip_s3_down.py

declare -a array
file="ip.txt"
while IFS= read -r line
do
    # display $line or do somthing with $line
    array+=( "$line" )
    
    #printf '%s\n\n' "${array[@]}"
    done <"$file"

bbbtime="$(date -d @"${array[1]}")"


printf 'IP Updated: %s\n' "$bbbtime"
echo "Updated $(($(date +%s) - ${array[1]})) seconds ago." 
printf 'Current BBB IP is %s\n' "${array[0]}"
    
read -p "Do you want to connect? " -n 1 -r
echo    # (optional) move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then
   sshpass -p PASSWORD ssh -o StrictHostKeyChecking=no debian@"${array[0]}"

#   ssh debian@"${array[0]}"   

fi

