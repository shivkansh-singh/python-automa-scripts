import boto3
import os

ec2=boto3.resource("ec2")

key_name="python1230"

key_pair=ec2.create_key_pair(KeyName=key_name)
print(key_pair.key_material)
with open(f"{key_name}.pem","w") as outputfile:
    outputfile.write(key_pair.key_material)

os.chmod(f"{key_name}.pem",0o400)

print("Key Generation successfully done")
print("key permissions changed successfully")
print(f"key ------> {key_name}.pem")
