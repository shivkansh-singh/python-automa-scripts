from fabric.api import *
import os
f = open("inventory","r")
env.hosts= f.readlines()
f.close()
#env.hosts=["192.168.161.129","192.168.161.130"]
env.user = "student"
env.password = os.getenv("USERPASS")

def storage():
    run("lsblk")
    run(" df -h")

def check_kernel():
    run("uname -r")

env.roledefs ={"serverb":['192.168.161.129'],"webservers":['192.168.161.130','192.168.161.129']}

@roles ('webservers')
def uptime():
    run("uptime")
