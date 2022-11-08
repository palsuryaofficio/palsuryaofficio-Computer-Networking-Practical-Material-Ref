import socket
import os
BUFFER_SIZE = 4096
s = socket.socket()
s.bind(("127.0.0.1", 5001))
s.listen(1)
print("Listening as 127.0.0.1:5001")
client_socket, address = s.accept()
print(f"{address[0]}:{str(address[1])} is connected to terminal")
while True:
    print("\nClient@Server>>", end=" ")
    command = client_socket.recv(BUFFER_SIZE).decode()
    print(command)
    if command == 'exit':
        break
    os.system(command)
print("Closing remote connectionwith client")
client_socket.close()
s.close()