import boto3

ACCESS_KEY = '' # aws account access key
SECRET_ACCESS_KEY = '' # aws account secret access key
BUCKET_NAME = '' # aws bucket name
DOWNLOAD_FILE = '' # s3 file name to download

s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_ACCESS_KEY)
s3.download_file(BUCKET_NAME, DOWNLOAD_FILE, 'ip.txt') # s3 bucket name, file to download, saved file name

