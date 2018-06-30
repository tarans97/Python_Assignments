print("***************Q U E S T  I O N- 3*******************")
from tkinter import*
root=Tk()
root.geometry("1600x800")
def close_window(root):
    root.destroy()
    

def transfer(root):
    lb1.configure(text="Hey, I am the New One")

f1=Frame(root,height=100,width=1600)
f1.pack(side=TOP)

lb1=Label(f1,font=("ALGERIAN",50),bg="yellow",bd=10,text="Hello World")
lb1.grid() #row=0,col=0
b1=Button(f1,padx=10,command=lambda:transfer(root),pady=15,font=("arial",10),bg="blue",text="Change Me",).grid()
b2=Button(f1,padx=10,command=lambda:close_window(root),pady=15,font=("arial",10),bg="blue",text="     Exit     ").grid()       
root.mainloop()
 
