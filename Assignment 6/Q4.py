import socket
import time
host = "13.0.1.219"
port = 9999
address = ((host, port))
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = input("Enter a message:").encode()
client.sento(message, address)
while True:
    data, address = client.recvfrom(1024)
    data = data.decode()
    print(data)