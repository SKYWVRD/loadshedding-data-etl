import json
import os
from botocore.vendored import requests
import boto3
from datetime import datetime

S3_OBJECT = boto3.client('s3')

def lambda_handler(event, context):
    MY_HEADERS = {'token': os.environ.get('token')}
    BUCKET_NAME = os.environ.get('bucket_name')
    response = requests.get(
        'https://developer.sepush.co.za/business/2.0/status', headers=MY_HEADERS)
    json_object = response.json()
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%m%d%Y %H%M")
    file_name = 'pending/' + formatted_datetime +'.json'
    S3_OBJECT.put_object(Bucket=BUCKET_NAME, Key=file_name, Body=json.dumps(json_object, indent=2, default=str))
    return {
        'statusCode': 200,
        'body': 'JSON Object Upload to S3 Bucket
    }
