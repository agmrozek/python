import os
import boto3

FILE_URL = 'https://{bucket}.s3.us-east-2.amazonaws.com/{filename}'
S3_BUCKET = 'pybites-tips'
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

def upload_to_s3(filepath, bucket=S3_BUCKET):
    session = boto3.Session(
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )
    s3 = session.resource('s3')
    ret = s3.Bucket(bucket).put_object(
        Key=os.path.basename(filepath),
        Body=open(filepath, 'rb'),
        ACL='public-read')
    return FILE_URL.format(bucket=bucket, filename=ret.key)

if __name__ == '__main__':
    upload_to_s3('my-tip-image.png')