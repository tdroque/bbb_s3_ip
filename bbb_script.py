#!/usr/bin/env python
# modified from http://elinux.org/RPi_Email_IP_On_Boot_Debian
import datetime
import netifaces as ni
import time
import boto3
from botocore.exceptions import ClientError

time.sleep(10)

ni.ifaddresses('eth0')
ipaddr = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']

ACCESS_KEY='' #aws account access key
SECRET_KEY='' #aws account secret access key

def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket
    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True                                                                                                                          

current_time = datetime.datetime.now()
current_time = int(current_time.timestamp())

ip_string = "{}\n {}\n".format(ipaddr,current_time)

with open('ip.txt', 'w') as file:
    file.write(ip_string)
    
upload =  upload_file('ip.txt', '', '') # file to upload, s3 bucket name, s3 item name

