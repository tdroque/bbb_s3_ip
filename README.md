
# BeagleBone IP

Scripts to upload Beaglbones eth0 IP address to a file on S3. And scripts to download the file, parse and auto ssh into the IP.

## BeagBone Files
```
bbb_s3_ip.py
```
Add AWS keys to bbb_s3_ip.py file, execute
Script can be set to auto run on startup

## Computer Files
```
ssh_script.sh, ip_s3_down.py
```
Add AWS keys to ip_s3_down.py file, ssh password to ssh_script.sh file
Execute ssh_script.sh, if you want to connect press y 
