#coding=gbk
import tkinter
from tkinter import *
from bubble_sort_function import *
from tkinter.filedialog import askdirectory
from tkinter.filedialog import *

def read_txt(filename_url):
	a = open(filename_url)
	txt_numbs = a.readline()
	return txt_numbs
	a.close()
	
def selectPath():
	filename = askopenfilename()
	v1.set(read_txt(filename))
		
root = Tk()
root.title("冒泡排序")
root.geometry("500x200")
frame = Frame(root)
frame.pack(padx=20,pady=20)

v1 = StringVar()
v2 = StringVar()


photo = tkinter.PhotoImage('rng.gif')

Label(frame,text="输入一个数组或打开一个数组文件:",\
			).grid(row=0,column=1)
Entry(frame,textvariable=v1,width=30,validate="focusout",\
			).grid(row=1,column=1)
Entry(frame,textvariable=v2,width=30,validate="key",state=DISABLED\
			).grid(row=2,column=1)


def calc():
	input_numbs = v1.get()
	numbs = input_numbs.split(",")
 
	if strOrNumber(numbs):	
		numb_lists = numbs
		for n in range(len(numbs)):
			numb_lists[n] = int(numbs[n])	
		v2.set(bubble_sort(numbs))
	else:
		v2.set("请输入正确数值")
		v1.set("")
		
Button(frame,text="浏览文件",command=selectPath).grid(row=1,column=2,pady=5)	
Button(frame,text="开始排序",command=calc).grid(row=2,column=2,pady=20,padx=10)
	
mainloop()		
	

