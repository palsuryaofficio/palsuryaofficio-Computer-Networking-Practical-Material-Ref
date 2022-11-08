import socket
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(("127.0.0.1", 9090))
data = input()
c.send(data.encode())
dataFromServer = c.recv(1024)
print(dataFromServer.deocode())
c.close()