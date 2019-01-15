
import socket
from socket import *
from threading import Thread

HOST = 'localhost'
PORT =12345
BUFSIZE=1024
ADDR=(HOST,PORT)
print(ADDR)
Sock = socket(AF_INET,SOCK_STREAM)
Sock.bind(ADDR)
Sock.listen(5)
print("Server 127.0.0.2 Listening...")

mydict=dict()
mylist=list()

def tell0thers(mynum,whattosay):
    for c in mylist:
        if c.fileno() != mynum:
            try:
                c.send(whattosay.encode())
            except:
                pass

def subTHreadIn(myconnection,connNumber):
    nickname = myconnection.recv(BUFSIZE).decode()
    mydict[myconnection.fileno()]=nickname
    mylist.append(myconnection)
    print('Connection',connNumber,'has nickname: ',nickname)
    while True:
        try:
            recveMsg =myconnect.recv(BUFSIZE).decode()
            if not recveMsg:
                pass
            else:
                print(mydict[connNumber],':',recceMsg)
                tell0thers(connNumber,mydict[connNumber]+':'+recveMsg)
        except(OSError,ConnectionResetError):
            try:
                mylist.remmove(myconnection)
            except:
                pass
            print(mydict[connNumber],'exit',len(mylist),'person left')
            tell0thers(connNumber,'[Remind:'+mydict[connNumber]+'has left the chatting room]')
            myconection.close()
            return

while True:
    connection,addr=Sock.accept()
    print('Accept a new connection',ADDR,connection.fileno())
    try:
        buf = connection.recv(BUFSIZE).decode()
        if buf == '1':
            connection.send(b'Welcime to server!')

            mythread = Thread(target=subThreadIn,args=(connection,connection.fileno()))
            mythread.setDaemon(True)
            mythread.start()
        else:
            connection.send(b'please go out!')
            connection.close()
    except:
        pass

