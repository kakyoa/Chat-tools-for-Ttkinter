#coding=gbk
from tkinter import *

root=Tk()
root.title('����Ԥ�����ݴ�����')
root.geometry('800x450')

def openfile():
	filename = str(e1.get())
	try:
		with open(filename) as f:
			for each_line in f:
				text.insert(INSERT,each_line)               
	except OSError as reason:
		print('�ļ������ڣ�\n�����������ļ���'+str(reason))
            
topFrame = Frame(root,bd=1, relief=SUNKEN)
topFrame.pack(fill=BOTH)

bottomFrame = Frame(root,bd=1, relief=SUNKEN)
bottomFrame.pack(fill=BOTH)

label=Label(topFrame,text="�ļ�����")
label.grid(row=0,column=0, sticky=W)

v1=StringVar()
e1=Entry(topFrame,textvariable=v1)
e1.grid(row=0,column=1,sticky=W)

b1=Button(topFrame,text="ȷ��",command=openfile)
b1.grid(row=0,column=2,padx=5,sticky=W)

text = Text(bottomFrame, height=600)
text.pack(fill=BOTH)


mainloop()
