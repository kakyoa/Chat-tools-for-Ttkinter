#coding=gbk
import socket
import tkinter
from tkinter import *
import time
import threading 

def main():
	filename = "record.txt"
	
	t = Tk()
	t.title('私聊神器-服务端')
	frmLT = Frame(width=500, height=320, bg='white')
	frmLC = Frame(width=500, height=150, bg='white')
	frmLB = Frame(width=500, height=30)
	frmRT = Frame(width=200, height=500)

	txtMsgList = Text(frmLT)
	txtMsgList.tag_config('greencolor', foreground='#008C00')
	txtMsg = Text(frmLC)
			
	host = socket.gethostname()
	port = 12345
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.bind((host,port))
	s.listen(5)

#	sock=None
#	addr=None
	sock,addr = s.accept()
	
	def server_thread():
#		sock,addr = s.accept()
#		print("111")
		while 1:
			info = sock.recv(1024).decode()
			if not info:
#				print("222")
				continue
			else:
#				info = "你对象：" + info
				strMsg = '你对象:' + time.strftime("%Y-%m-%d %H:%M:%S",
											  time.localtime()) + '\n '
				txtMsgList.insert(END, strMsg, 'greencolor')
				txtMsgList.insert(END,info)
				txtMsg.delete('0.0', END)
				
				file_txt = strMsg + info + "\n"
				with open(filename,'a') as file_write:
					file_write.write(file_txt)				
#				txtMsgList.insert(END,info)		
			 
	def sendMsg():
		send_mes = txtMsg.get('0.0','end')
		sock.send(send_mes.encode())
		
		
		
		
		
		
		
		
		
		
		
		
		
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
	btnRecord.grid(row=2,column=2)
	btnCancel.grid(row=2, column=1)
	lblImage.grid()
	txtMsgList.grid()
	txtMsg.grid()
	
	td=threading.Thread(target=server_thread,args=()) 
	td.start() 
	t.mainloop()

if __name__ =='__main__':
	main()
	
