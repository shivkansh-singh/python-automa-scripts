import socket

class Scanner():
    def __init__(self,ip):
        self.ip = ip
        self.open_ports = []

    def add_port(self,port): #to append the open port in the  open ports list
        self.open_ports.append(port)





    def scan(self,lowerport,upperport): #to check for hundreds or thousands of ports
        for port in range(lowerport,upperport+1):
            if self.check_open(port):
                self.add_port(port)



    def check_open(self,port): ##to chech whether the port is open or not
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result = s.connect_ex((self.ip,port))
        s.close()
        return result ==0
       
def main():
    ip=input("Enter the IP to port scan: ")
    myscan= Scanner(ip)
    myscan.scan(1,1000)
    print(myscan.open_ports)

main()
