import socket

s= socket.socket()
host = 'localhost'
port = 12345
s.connect((host,port))
print('Linked')
info = ''

while info != 'exit':
    print('SCIENCE:'+info)
    send_mes=input()
    s.send(send_mes.encode())
    if send_mes =='exit':
        break
    info = s.recv(1024).decode()
    
s.close()

