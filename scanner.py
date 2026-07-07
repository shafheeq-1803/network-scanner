import socket

ip = input("Enter IP Address: ")

ports = [21, 22, 23, 25, 53, 80, 110, 443]

for port in ports:

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    result = sock.connect_ex((ip, port))

    if result == 0:
        print(f"Port {port} is OPEN")

    else:
        print(f"Port {port} is CLOSED")

    sock.close()