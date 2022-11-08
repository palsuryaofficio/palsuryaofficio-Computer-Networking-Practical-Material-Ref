import socket
import os
BUFFER_SIZE = 4096
c = socket.socket()
print("Connecting to 127.0.0.1:5001")
c.connect(("127.0.0.1", 5001))
print("Connectd to Server Terminal")
while True:
    command = input("\nServer>>")
    c.sendall(command.encode())
    if command == 'exit':
        break
print("Closing remote connection with server")
c.close()