import socket
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(("127.0.0.1", 9090))
data = c.recv(1024).decode()
print(data, end=" ")
otp = input()
c.send(otp.encode())
data = c.recv(1024).decode()
print(data)
if data == "You are authenticated":
    data = input("Enter text: ")
    c.send(data.encode())
    data = c.recv(1024).decode()
    print("Server: ", data)
else:
    c.close()