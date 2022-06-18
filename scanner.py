import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "76.76.21.142"
port = 80

def scanner(host, port):
    if sock.connect_ex((host, port)):
        print(f"Port {port} is closed")
    else:
        print(f"Port {port} is open")

scanner(host, port)