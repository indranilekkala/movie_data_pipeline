import os
import boto3
from dotenv import load_dotenv

load_dotenv()

session = boto3.session.Session(
    aws_access_key_id=os.getenv("S3_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("S3_SECRET_KEY"),
    region_name=os.getenv("S3_REGION")  # optional if using IAM roles
)

s3 = session.client("s3")

def upload_to_s3(file_path, bucket_name, s3_key):
    s3.upload_file(file_path, bucket_name, s3_key)


print("✅ CSV files uploaded to S3.")