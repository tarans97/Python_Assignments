print("***************Q U E S T  I O N- 2*******************")
from tkinter import* #root is variable
root=Tk()

root.geometry() #giving size to window
root.title("Hello World")


def close_window(root):
    print("Hi")
    
f1=Frame(root,height=100,width=1600)
f1.pack(side=TOP)
lb1=Label(f1,font=("ALGERIAN",50),bg="yellow",bd=10,text="Hello World")
lb1.grid() #row=0,col=0
b1=Button(f1,padx=25,command=lambda:close_window(root),pady=15,font=("arial",10),bd=10,bg="blue",text="Exit").grid(row=1,column=0)
root.mainloop()

