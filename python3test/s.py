#coding=gbk
from tkinter import *
import time
import tkinter

print("000")
filename='recordMsg.txt'

t = Tk()
t.title('正在与python聊天')
print("111")
frmLT = Frame(width=500, height=320, bg='white')
frmLC = Frame(width=500, height=180, bg='white')
frmLB = Frame(width=500, height=30)
frmRT = Frame(width=200, height=500)

txtMsgList = Text(frmLT,bg='#d7eef5')
txtMsgList.tag_config('color', foreground='#ff66ad',font='14px')#创建tag
txtMsg = Text(frmLC);	
	
def sendMsg():
	strMsg = '我:'+ time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) + '\n '
	txtMsgList.insert(END, strMsg, 'color')
	txtMsgList.insert(END, txtMsg.get('0.0', END))
	with open(filename,'a')as file_object:
		file_object.write(strMsg+txtMsg.get('0.0', END)+'\n')
	
	txtMsg.delete('0.0', END)
		
def cancelMsg():
	txtMsg.delete('0.0', END)
		
def recordMsg():
	with open(filename) as readMsg:
		txtMsgList.delete('0.0', END)
		txtMsgList.insert(END, readMsg.read())
			
def sendMsgEvent(event): 
	if event.keysym == "Up":
		sendMsg()


	
txtMsg.bind("<KeyPress-Up>", sendMsgEvent)
btnSend = Button(frmLB, text='发送', width = 8, command=sendMsg)
btnCancel = Button(frmLB, text='取消', width = 8, command=cancelMsg)
btnRecord = Button(frmLB, text='查看历史', width = 8, command=recordMsg)
imgInfo = PhotoImage("python.png")
lblImage = Label(frmRT, image = imgInfo)
lblImage.image = imgInfo


frmLT.grid(row=0, column=0, columnspan=2, padx=1, pady=3,)
frmLC.grid(row=1, column=0, columnspan=2, padx=1, pady=3)
frmLB.grid(row=2, column=0, columnspan=2,sticky=E)
frmRT.grid(row=0, column=2, rowspan=3, padx=2, pady=3)
	  

frmLT.grid_propagate(0)
frmLC.grid_propagate(0)
frmLB.grid_propagate(2)
frmRT.grid_propagate(0)

btnSend.grid(row=2, column=0)
btnCancel.grid(row=2, column=1)
btnRecord.grid(row=2, column=2)
lblImage.grid()
txtMsgList.grid()
txtMsg.grid()

t.mainloop()
