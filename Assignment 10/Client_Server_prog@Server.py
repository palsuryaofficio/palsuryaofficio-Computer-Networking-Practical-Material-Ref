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


def encodeData(data, key):
    l_key = len(key)
    appended_data = data + '0' * (l_key-1)
    remainder = mod2div(appended_data, key)
    codeword = data + remainder
    return codeword


s = socket.socket()
port = 12345
s.connect(('127.0.0.1', port))
input_string = input("Enter data you want to send: ")
data = ("".join(format(ord(X), 'b') for X in input_string))
print("Entered data in binary format: ", data)
key = '1001'
ans = encodeData(data, key)
print("Encoded data to be sent to server in binary format: ", ans)
s.sendto(ans.encode(), ('127.0.0.1', 12345))
print("Received feedback from server: ", s.recv(1024).decode())
s.close()