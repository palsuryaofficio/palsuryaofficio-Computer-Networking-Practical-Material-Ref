import socket
import time
host = "13.0.1.219"
port = 9999
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((host, port))
message, address = server.recvfrom(1024)
message = message.decode()
print(message)
while True:
    t = time.localtime()
    current_time = time.strftime("%H%M%S", t)
    current_time = current_time.encode()
    server.sendto(current_time, address)
    time.sleep(5)