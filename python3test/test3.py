#coding=gbk
from tkinter import*
import time,socket,threading,sys

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
def main():
	#initial

	s.connect(('localhost',5000))
	try:
		machCode='test'
		s.send(machCode.encode())
	except ConnectionRefuseError:
		print('Warning:?The?MATCH?CODE?is?error!')
		sys.exit()
	except KeyboardInterrupt:
		print('\nNotice:?You?have?quited?the?system!')
		sys.exit()
	except ConnectionAbortedError:
		print('Notice:Server has closed your connection!')
		sys.exit()
	except ConnectionResetError:
		print('Warnning:The server is closed!')
		sys.exit()
		
	try:
		print(s.recv(1024).decode())
		nickname=input('Notice:Input your nickname:')
		#nickname='test'
		s.sendall(nickname.encode())
	except KeyboardInterrupt:
		print('\nNotice:You have quited the system!')
		sys.exit()
	except ConnectionResetError:
		print('Warinning:The server is closed!')
		sys.exit()
		
def recvMsg(factor=0):#receive message
	try:
		receContent=s.recv(1024).decode()
	except(OSError,ConnectionAbortedError,ConnectionResetError):
		recvContent='Warinning:SERVER ERROR'
	else:
		if recvContent:
			name,content=recvContent.split('',1)
			strMsg=name+''+time.strftime("%Y-%m-%d%H:%M:%S",time.localtime())+'\n'+content
			txtMsgList.insert(END,strMsg)
		else:
			pass
		timer=theading.Timer(0.1,recvMsg)
		timer.setDaemon(True)
		timer.start()
	
			
#sendMessage

def sendMsg():
	content=txtMsg.get('0.0',END)
	if len(content)!=1:
		try:
			s.sendall(content.encode())
		except ConnectionAbortedError:
			strMsg='Notice:' + time.strftime("%Y-%m-%d%H:%H:%S",time.localtime()) + \
							'\n'+'Server has closed your connection!\n'
			txtMsgList.insert(END,strMsg)
		except ConnectionResetError:
			strMsg='Notice:'+time.strftime("%Y-%m-%d%H:%H:%S",time.localtime())+'\n'+'Server is closed!\n'
			txtMsgList.insert(END,strMsg)
		else:
			strMsg='?'+time.strftime("%Y-%m-%d%H:%H:%S",time.localtime())+'\n'+content
			txtMsgList.insert(END,strMsg)
	txtMsg.delete('0.0',END)
def cancelMsg():
	txtMsg.delete('0.0',END)
def sendMsgEvent(event):
	if event.keysym=='Up':
		sendMsg()
#creat window
t=Tk()
t.title('Chatting room')

#creat frame
frmLT=Frame(width=500,height=320,bg='white')
frmLC=Frame(width=500,height=150,bg='white')
frmLB=Frame(width=500,height=30)
frmRT=Frame(width=200,height=50)

#creat controls
txtMsgList=Text(frmLT)
txtMsgList.tag_config('greencolor',foreground='#008C00')
txtMsg=Text(frmLC)
txtMsg.bind("KeyPress-Up",sendMsgEvent)
btnSend=Button(frmLB,text='发送',width=8,command=sendMsg)
btnCancel=Button(frmLB,text='取消',width=8,command=cancelMsg)
imgInfo=PhotoImage(file='timg2.gif')
lblImage=Label(frmRT,image=imgInfo)
lblImage.image=imgInfo

#layout
frmLT.grid(row=0,column=0,columnspan=2,padx=1,pady=3)
frmLC.grid(row=1,column=0,columnspan=2,padx=1,pady=3)
frmLB.grid(row=2,column=0,columnspan=2)
frmRT.grid(row=0,column=2,rowspan=2,padx=1,pady=3)
#fixed size
frmLT.grid_propagate(0)
frmLC.grid_propagate(0)
frmLB.grid_propagate(0)
frmRT.grid_propagate(0)

btnSend.grid(row=2,column=0)
btnCancel.grid(row=2,column=1)
lblImage.grid()
txtMsgList.grid()
txtMsg.grid()

#recv loop
timer=threading.Timer(0.1,recvMsg)
timer.setDaemon(True)
timer.start()

#main loop
t.mainloop()
 
if _name_ == '_main_':
	main()










































	
		
		
		
		
			





















				
				
				
				
				
	
		
		
		
		
		
		
		
		
		
		
		
		
			
		

