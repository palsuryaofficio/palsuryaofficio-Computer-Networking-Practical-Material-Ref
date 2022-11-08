import socket
def xor(a, b):
    result=[]
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return "".join(result)


def mod2div(dividend, divisor):
    pich = len(divisor)
    temp = dividend[0:pich]
    while pich < len(dividend):
        if temp[0] == '1':
            temp = xor(divisor, temp) + dividend[pich]
        else:
            temp = xor('0'*pich, temp) + dividend[pich]
        pich+=1
        if temp[0] == '1':
            temp = xor(divisor, temp)
        else:
            temp = xor('0'*pich, temp)
        checkword = temp
    return checkword

def decodeData (data, key):
    l_key = len(key)
    appended_data = data.decode() + '0'*(l_key-1)
    remainder = mod2div(appended_data, key)
    return remainder


c = socket.socket()
print("Socket successfully created")
port = 12345
c.bind(('127.0.0.1', port))
print("Socket binded to %s" %(port))
c.listen(c)
print("Socket is listening")
while True:
    c.addr = c.accept()
    print("Connected to ", c.addr)
    data = c.recv(1024)
    print("received: ", data.decode())
    if not data:
        break

key = '1001'
ans = decodeData(data, key)
print("Remainder aftre decoding is: " + ans)
temp = '0'* (len(key) - 1)
if ans==temp:
    c.sendto(("Thank You" + data.decode() + "Received").encode(), (('127.0.0.1', 12345)))
else:
    c.sendto(("error").encode(), ('127.0.0.1',12345))
    c.close()