import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.setdefaulttimeout(2)

host = input("[*] Enter The Host IP: ")
port = int(input("[*] Enter The Port To Scan: "))

def scanner(host, port):
    if sock.connect_ex((host, port)):
        print(f"Port {port} is closed")
    else:
        print(f"Port {port} is open")

scanner(host, port)