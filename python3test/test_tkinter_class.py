#coding=utf-8
# 简单的图形界面GUI（Graphical User Interface）
from tkinter import *
import tkinter.messagebox as messagebox
#from bubble_sort import *


class Application(Frame):  # 从Frame派生出Application类，它是所有widget的父容器
    def __init__(self, master=None):  # master即是窗口管理器，用于管理窗口部件，如按钮标签等，顶级窗口master是None，即自己管理自己
        Frame.__init__(self, master)
        self.pack()  # 将widget加入到父容器中并实现布局
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='bubblu')  # 创建一个标签显示内容到窗口
        self.helloLabel.pack()
        self.numinput = Entry(self)
        self.numinput.pack()
        self.bubbleButton = Button(self, text='sort',command=self.numinput) # 创建一个bubble_sort按钮，实现点击即开始排序
        self.bubbleButton.pack()
        self.input = Entry(self)  # 创建一个输入框，以输入内容
        self.input.pack()
	def numinput(self):
		numlist =app.createWidgets().numinput.get().split(",")  # 获取输入的内容
		app.createWidgets().input.set(bubble(numlist))
app = Application()

app.master.title("hello")  # 窗口标题

app.mainloop()  # 主消息循环
