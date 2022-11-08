import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 9090))
s.listen()
c, cip = s.accept()
c.send(c.recv(1024))
s.close()