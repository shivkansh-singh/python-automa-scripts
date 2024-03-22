import boto3

s3= boto3.resource("s3")
bucket_name= "networknutsasd"
s3_bucket=s3.Bucket(bucket_name)
n=0
for item in s3_bucket.objects.all():
    n=n+1
    print(f"{n}.{item.key}")

print(f"Total objects uploaded = {n}")
    
