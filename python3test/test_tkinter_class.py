#coding=utf-8
# �򵥵�ͼ�ν���GUI��Graphical User Interface��
from tkinter import *
import tkinter.messagebox as messagebox
#from bubble_sort import *


class Application(Frame):  # ��Frame������Application�࣬��������widget�ĸ�����
    def __init__(self, master=None):  # master���Ǵ��ڹ����������ڹ����ڲ������簴ť��ǩ�ȣ���������master��None�����Լ������Լ�
        Frame.__init__(self, master)
        self.pack()  # ��widget���뵽�������в�ʵ�ֲ���
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='bubblu')  # ����һ����ǩ��ʾ���ݵ�����
        self.helloLabel.pack()
        self.numinput = Entry(self)
        self.numinput.pack()
        self.bubbleButton = Button(self, text='sort',command=self.numinput) # ����һ��bubble_sort��ť��ʵ�ֵ������ʼ����
        self.bubbleButton.pack()
        self.input = Entry(self)  # ����һ�����������������
        self.input.pack()
	def numinput(self):
		numlist =app.createWidgets().numinput.get().split(",")  # ��ȡ���������
		app.createWidgets().input.set(bubble(numlist))
app = Application()

app.master.title("hello")  # ���ڱ���

app.mainloop()  # ����Ϣѭ��
