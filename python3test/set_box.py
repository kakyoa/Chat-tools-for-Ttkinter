import Tkinter
import Tkinter.messagebox

top = Tkinter.Tk()

def helloCallBack():
    tkMessageBox.showinfo("Hello Python", "Hello Runoob")


B = Tkinter.Button(top, text="点我", command=helloCallBack)

B.pack()
top.mainloop()
