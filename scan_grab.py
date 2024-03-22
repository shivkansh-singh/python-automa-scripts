from port-scanner import Scanner 
from grabber import Grabber

def main():
    ip = input("Enter IP to banner grabbing: ")
    scanner = Scanner(ip)
    scanner.scan(1,10000)
    for port in scanner.open_ports:
        try:
            grabber = Grabber(ip,port)
            print(f"{port} ----- {grabber.read()}")
            grabber.close()
        except:
            print(f"Error: {port} is not giving any output.")

main()
