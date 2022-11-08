import socket
import time
host = "127.0.0.1"
port = 9999
addr = (host, port)
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = input("Enter a message: ").encode()
client.sendto(message, addr)
while True:
    data, addr = client.recvfrom(1024)
    data = data.decode()
    print(data)