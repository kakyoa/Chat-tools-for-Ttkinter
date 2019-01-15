#coding=gbk
from tkinter import *
from bubble_sort_function import *

root = Tk()
root.title("冒泡排序")
frame = Frame(root)
frame.pack(padx=40,pady=40)
v1 = StringVar()
v2 = StringVar()

def test(content):
	if content == "":
		return True
	else:
		return False
		
testCMD = root.register(test)
Label(frame,text="请输入一组数字：").grid(row=0,column=0)
Entry(frame,textvariable=v1,width=30,validate="focusout",\
			).grid(row=1,column=0)
Entry(frame,textvariable=v2,width=30,validate="key",\
			validatecommand=(testCMD,'%P')).grid(row=3,column=0)


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
		
	
Button(frame,text="开始排序",command=calc).grid(row=2,column=0,pady=5)
	
mainloop()		
	

