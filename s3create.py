import boto3

client = boto3.client('s3')

bucket_name = input("Enter the bucket name to create: ")
bucket_location = input("Enter the bucket location: ")

print("Starting S3 Bucket Creation Process")

response = client.create_bucket(Bucket=bucket_name,CreateBucketConfiguration={"LocationConstraint":bucket_location})
print(response)
#print("S3Bucket created successfully!")

#print(f"S3 Bucket ----> {bucket_name}")
#print(f"S3 Bucket Location ----> {bucket_location}")
