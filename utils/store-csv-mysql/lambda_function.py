import os
import csv
import boto3
import pg8000
from urllib.parse import unquote_plus

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # RDS settings
    db_host  = ''
    db_name = ''
    db_user = 'admin'
    db_password = 'secret01'
    db_table = 'salaries'

    # S3 settings
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = unquote_plus(event['Records'][0]['s3']['object']['key'])

    # create connection to the database
    conn = pg8000.connect(
        host=db_host, user=db_user, password=db_password, ssl_context=True)
    cursor = conn.cursor()

    # download the CSV file
    csv_file = '/tmp/tmpfile'
    s3_client.download_file(bucket_name, file_key, csv_file)

    # read the CSV file and insert each row into the database
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        for row in reader:
            # replace empty strings with None
            row = [None if cell == '' else cell for cell in row]
            query = f"INSERT INTO {db_table} ({','.join(headers)}) VALUES ({','.join(['%s'] * len(row))})"
            cursor.execute(query, tuple(row))
    conn.commit()

    # close connection
    cursor.close()
    conn.close()

    # remove the temporary file
    os.remove(csv_file)

    # Delete file from S3 bucket
    s3_client.delete_object(Bucket=bucket_name, Key=file_key)

    return {
        'statusCode': 200,
        'body': 'Los datos se han insertado en la base de datos!'
    }
