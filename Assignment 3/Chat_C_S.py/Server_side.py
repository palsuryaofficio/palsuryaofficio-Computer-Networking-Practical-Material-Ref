import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 9090))
s.listen()
while True:
    c, cip = s.accept()
    data = c.recv(1024).deocde()
    print("Client: ", data)
    data = input("Enter text: ")
    c.send(data.encode())