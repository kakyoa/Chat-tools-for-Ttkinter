#coding=gbk
from tkinter import * 
import socket
import threading 
import time 


topWv = Tk()
topWv.title("connect") 
topWv.geometry('500x800') 
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
server.bind(('localhost', 20000)) 
server.listen(5)

tcpSock=None
addr=None

message_var = StringVar()
message_e=Entry(topWv,textvariable=message_var) 
message_var.set('hello') 
message_e.place(x=10,y=340,anchor=NW)

def send(): 
   
    global server 
    global message_var 
    message_str = "".join(message_var.get()) 
    print(message_str) 
    global tcpSock
    global addr
    tcpSock.send(message_str) 
    pass 
sendBtn= Button(topWv,text='发送',bg='green',width=10,height=1,command=send); 
sendBtn.place(x=150,y=730,anchor=NW) 
t=Text(topWv,width=50,height=35) 
t.place(x=10,y=100,anchor=NW) 
def server_thread(): 
   global server 
   global tcpSock
   global addr 
   global t 
   tcpSock, addr = server.accept(); 
   while 1: 
       print('wait data') 
       data=tcpSock.recv(1024) 
       print(addr) 
       if not data: 
           continue 
       else: 
           print(data) 
t=threading.Thread(target=server_thread,args=()) 
t.start() 
topWv.mainloop() 
