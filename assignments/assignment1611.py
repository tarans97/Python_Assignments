from tkinter import *
from tkMessageBox import *


root = Tk()

def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Hello World")

B =Button(top, text ="Hello", command = helloCallBack)

B.pack()
root.mainloop()
