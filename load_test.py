import os
import boto3
from dotenv import load_dotenv 

load_dotenv()

aws_access_key = os.getenv('AWS_ACCESS_KEY')
aws_secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
bucket = os.getenv('bucket')

# print(bucket)

s3_client = boto3.client(
    's3'
    , aws_access_key_id = aws_access_key
    , aws_secret_access_key = aws_secret_key
)

filename = 'data/2025-11-05T15-26-31.json'
s3filename = '2025-11-05T15-26-31.json'

s3_client.upload_file(filename, bucket, s3filename)