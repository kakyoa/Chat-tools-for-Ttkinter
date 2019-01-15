#coding=gbk
import socket
import tkinter
from tkinter import *
import time
import threading

filename = "recordf.txt"

t = Tk()
t.title('私聊神器-客户端')
frmLT = Frame(width=500, height=320, bg='white')
frmLC = Frame(width=500, height=150, bg='white')
frmLB = Frame(width=500, height=30)
frmRT = Frame(width=200, height=500)
txtMsgList = Text(frmLT)
txtMsgList.tag_config('greencolor', foreground='#008C00')
txtMsg = Text(frmLC)

s= socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host,port))

def server_thread():
	while 1:
		info = s.recv(1024).decode()
		if not info:
			continue
		else:
			strMsg = '范冰冰:' + time.strftime("%Y-%m-%d %H:%M:%S",
										  time.localtime()) + '\n '
			txtMsgList.insert(END, strMsg, 'greencolor')
			txtMsgList.insert(END, info)
			txtMsg.delete('0.0', END)
			file_txt = strMsg + info + "\n"
			with open(filename,'a') as file_write:
				file_write.write(file_txt)									

def sendMsg():
	send_mes = txtMsg.get('0.0','end')
	s.send(send_mes.encode())	
	strMsg = '我:' + time.strftime("%Y-%m-%d %H:%M:%S",
                                  time.localtime()) + '\n '
	txtMsgList.insert(END, strMsg, 'greencolor')
	txtMsgList.insert(END, txtMsg.get('0.0', END))
	file_txt = strMsg + txtMsg.get('0.0', END) + "\n"
	txtMsg.delete('0.0', END)
	with open(filename,'a') as file_write:
		file_write.write(file_txt)
			
def cancelMsg():
  txtMsgList.delete('0.0', END)

def sendMsgEvent(event): 
  if event.keysym == "Up":
    sendMsg()
    
def recordMsg():
	with open(filename) as file_read:
		txtMsgList.delete('0.0',END)
		txtMsgList.insert(END,file_read.read())
	    

txtMsg.bind("<KeyPress-Up>", sendMsgEvent)

btnSend = Button(frmLB, text='发送', width = 8, command=sendMsg)
btnCancel = Button(frmLB, text='清空消息', width = 8, command=cancelMsg)
btnRecord = Button(frmLB, text='历史记录', width = 8, command=recordMsg)

imgInfo = PhotoImage(file = "timg2.gif")
lblImage = Label(frmRT, image = imgInfo)
lblImage.image = imgInfo
  
frmLT.grid(row=0, column=0, columnspan=2, padx=1, pady=3)
frmLC.grid(row=1, column=0, columnspan=2, padx=1, pady=3)
frmLB.grid(row=2, column=0, columnspan=2)
frmRT.grid(row=0, column=2, rowspan=3, padx=2, pady=3)
 
frmLT.grid_propagate(0)
frmLC.grid_propagate(0)
frmLB.grid_propagate(0)
frmRT.grid_propagate(0)

btnSend.grid(row=2, column=0)
btnCancel.grid(row=2, column=1)
btnRecord.grid(row=2,column=2)
lblImage.grid()
txtMsgList.grid()
txtMsg.grid()

td=threading.Thread(target=server_thread,args=()) 
td.start() 
t.mainloop()




