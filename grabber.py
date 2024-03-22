import socket

class Grabber:
    def __init___(self,ip,port):
        self.ip = ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.settimeout(2)
        self.socket.connect((self.ip,self.port)

    def read(self,lenght=1024):
        return self.socket.recv(length)

    def close(self):
        self.socket.close()
