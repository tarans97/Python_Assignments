print("***************Q U E S T  I O N- 4*******************")
from tkinter import*
root=Tk()
root.geometry("1600x800") 
def fn():
    print(e1.get())
f1=Frame(root,height=10,width=100)
f1.pack(side=TOP)
lb1=Label(f1,font=("ALGERIAN",20),bg="yellow",bd=10,text="User Input")
lb1.grid()
e1=Entry(f1,width=45,bd=10,bg="Sky blue").grid(row=1,column=0)
b1=Button(f1,padx=25,command=lambda:fn(),pady=15,font=("arial",10),bd=10,bg="blue",text="Print").grid(row=2,column=0)





root.mainloop()
 
