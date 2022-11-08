import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 9090))
s.listen()
c, cip = s.accept()
c.send("Enter OTP: ".encode())
otp = c.recv(1024).decode()
if otp == '8894':  #can edit this otp
    c.send("You are authenticated".encode())
    data = c.recv(1024).decode()
    print("Client: ", data)
    data = input("Enter text: ")
    c.send(data.encode())
else:
    c.send("You are authenticated". encode())
s.close()