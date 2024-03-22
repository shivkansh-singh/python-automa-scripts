import boto3

def upload_file(file_path,bucket_name,object_name=None):
    if object_name is None:
        object_name = file_path
    s3 = boto3.client("s3")
    try:
        s3.upload_file(file_path,bucket_name,object_name)
    except Exception as e:
        print(e)
    else:
        print(f"File {file_path} ----> {bucket_name}")
        print(f"Object Name is {object_name}")

upload_file("/etc/hosts","networknutsasd","hosts")
