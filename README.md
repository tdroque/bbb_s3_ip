
# BeagleBone IP

Scripts to upload Beaglbones eth0 IP address to a file on S3. And scripts to download the file, parse and auto ssh into the IP.

## BeagBone Files
```
bbb_s3_ip.py
```
Add AWS keys to bbb_s3_ip.py file, execute

## Computer Files
```
ssh_script.sh, ip_s3_down.py
```
Add AWS keys to ip_s3_down.py file, ssh password to ssh_script.sh file
Execute ssh_script.sh, if ip looks correct press y to connect
