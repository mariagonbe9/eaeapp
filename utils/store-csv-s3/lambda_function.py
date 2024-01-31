import json
import base64
import boto3

s3 = boto3.client('s3')
BUCKET_NAME = 'eaebucket'

def lambda_handler(event, context):
    content_type = event['headers']['content-type']
    boundary = content_type.split(';')[1].split('=')[1].strip()
    body = event['body']

    parts = body.split("--" + boundary)

    # Find part with file content
    for part in parts:
        if 'filename=' in part:
            file_part = part

    file_data = file_part.split('\r\n\r\n')[1].rsplit('\r\n', 1)[0]

    # Save file to S3
    s3.put_object(Body=file_data, Bucket=BUCKET_NAME, Key='salaries.csv')

    # Construct response
    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": True,
        },
        "body": json.dumps({"message": "File uploaded successfully"})
    }

    return response
