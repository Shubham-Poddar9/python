from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
root=Tk()
root.title("DENOMINATION COUNTER APPLICATION")
root.geometry("500x500")
root.configure(bg="yellow")
a=Image.open("money.jpg")
a=a.resize((300,300))
s=ImageTk.PhotoImage(a)
label=Label(root,image=s)
label.place(x=7,y=5)
label1=Label(root,text="Welcome to the application!!!!.",bg="green",fg="blue")
label1.place(x=55,y=300)
def display():
    q=messagebox.showinfo("Alert!!!!!","Would like to continue")
    if q=="ok":
        topwin()
button=Button(text="Let's start!!",bg="purple",fg="white",command=display)
button.place(x=60,y=350)
def topwin():
    n=Toplevel()
    n.title("calculation window")
    n.geometry("400x400")
    n.configure(bg="pink")
    label2=Label(n,text="enter your amount")
    u=Entry(n)
    label3=Label(n,text="This is the result")
    l1=Label(n,text="2000")
    l2=Label(n,text="500")
    l3=Label(n,text="100")
    e1=Entry(n)
    e2=Entry(n)
    e3=Entry(n)
    def calculate():
        global amount
        amount=int(u.get())
        note2000=amount//2000
        amount=amount%2000
        note500=amount//500
        amount=amount%500
        note100=amount//100
        amount=amount%100

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e1.insert(END, str(note2000))
        e2.insert(END, str(note500))
        e3.insert(END, str(note100))
    b1=Button(n,text="calculate",command=calculate)
    label2.pack()
    u.pack()
    b1.pack()
    label3.pack()
    l1.pack()
    e1.pack()
    l2.pack()
    e2.pack()
    l3.pack()
    e3.pack()
    n.mainloop()
root.mainloop()