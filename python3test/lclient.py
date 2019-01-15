from socket import *
from threading import Thread

HOST = 'localhost'
PORT =12345
BUFSIZE=1024
ADDR=(HOST,PORT)
print(ADDR)
Sock = socket(AF_INET,SOCK_STREAM)
Sock.connect(ADDR)

Sock.send(b'1')
print(Sock.recv(BUFSIZE).decode())
nickname=input("input your nackname: ")
Sock.send(nickname.encode())

def sendThreadFunc():
    while True:
        try:
            myword=input(">>>")
            myword=myword.encode('utf-8')
            print(Sock.recv(BUFSIZE).decode())
            Sock.send(myword)
        except ConnectionAbortedError:
            print('Warning! The connection is aborten')
        except ConnectionResetError:
            print("Warning! The connection is reset!")

def cecvThreadFunc():
    while True:
        try:
            otherword=Sock.recv(BUFSIZE)
            if otherword:
                print(otherword.decode())
            else:
                pass
        except ConnectionResetError:
            print("Warning! The connection is reset!")
        except ConnectionAbortedError:
            print("Warning! The coonnection is aborted!")

send1=Thread(target=sendThreadFunc)
recv1=Thread(target=cecvThreadFunc)
thread=[send1,recv1]

for t in thread:
    t.setDaemon(True)
    t.start()
    t.join()
