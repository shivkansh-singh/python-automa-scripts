import getpass

hostname = input("Enter your hostname or ip: ")
username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")
cmd = input(" Enter the command to execute: ")

from paramiko.client import SSHClient
from paramiko.client import AutoAddPolicy
def myssh():
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy)

    client.connect(hostname, port=22, username=username, password=password)
    stdin, stdout, stderr = client.exec_command(cmd)
    print(stdout.read().decode())
    print(stderr.read().decode())

    client.close()

myssh()
