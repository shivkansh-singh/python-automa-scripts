from paramiko.client import SSHClient
from paramiko.client import AutoAddPolicy

vms = [{'hostname':'192.168.161.129','username':'student','password':'redhat'},{'hostname':'192.168.161.130','username':'student','password':'redhat'}]
cmd = "df -h"

def multi_ssh(hostname,username,password,command):
     client=SSHClient()
     client.set_missing_host_key_policy(AutoAddPolicy)
     client.connect(hostname=hostname,port=22,username=username,password=password)
     stdin, stdout, stderr = client.exec_command(cmd)
     print(f"Server: {hostname}")
     print(stdout.read().decode())
     print(stderr.read().decode())
     print(client.close())
     print("-----------CONNECTION CLOSED-------------")
    

for vm in vms:
    multi_ssh(vm['hostname'],vm['username'],vm['password'],cmd)
