import socket
print("Host Name: ", socket.gethostname(),"\n")
print("IP Address: ", socket.gethostbyname(socket.gethostname()))