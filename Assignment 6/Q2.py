import socket
import time 
host = "127.0.0.1"
port = 9999
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
message, address = server.recvfrom(1024)
print(message)
while True:
    message, address = server.recvfrom(1024)
    message = message.decode()
    print(message)
    t = time.localtime()
    current_time = time.strftime("%H%M%S", t)
    current_time = current_time.encode()
    server.sendto(current_time, address)