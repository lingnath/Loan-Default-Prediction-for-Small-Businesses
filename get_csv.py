import boto3
from botocore import UNSIGNED
from botocore.config import Config

s3_client = boto3.client('s3', config=Config(signature_version=UNSIGNED))

s3_bucket = 'ds-projects-nl-public'

s3_client.download_file(s3_bucket, 'SBAnational.csv', 'SBAnational.csv')
