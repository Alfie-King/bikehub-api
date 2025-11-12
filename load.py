# importing packages
import os
import boto3
import sys
from dotenv import load_dotenv 

def load():
    load_dotenv()

    # loading aws keys
    aws_access_key = os.getenv('AWS_ACCESS_KEY')
    aws_secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
    bucket = os.getenv('bucket')

    # setting up s3 client 
    s3_client = boto3.client(
        's3'
        , aws_access_key_id = aws_access_key
        , aws_secret_access_key = aws_secret_key
    )

    # checking for any high level errors
    try:
        # checking access to the s3
        # try:
        #     s3_client.list_objects_v2(Bucket=bucket)
        # except:
        #     print('Access denied')
        #     sys.exit(1)
        
        # looping for each file in the data folder
        dir = 'data'
        file = [f for f in os.listdir(dir) if f.endswith('.json')]

        # checking if there are files in the data folder
        if len(file)>0:
            # if there are files uploads to s3 and removes for data folder
            filename = dir+'/'+file[0]
            s3filename = file[0]
            s3_client.upload_file(filename, bucket, s3filename)
            os.remove(filename)
        else:
            # if no prints fail message
            print('No files to upload')
    except Exception as e:
        # prints any errors that are occuring
        print(e)
        raise e