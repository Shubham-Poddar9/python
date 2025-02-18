from tkinter import *
from tkinter import messagebox
window=Tk()
window.title("message box") 
window.geometry("400x400")
def display():
    messagebox.showwarning("Alert box","Dont use this this is full of virus")
button=Button(text="WARNING!!",bg="green",fg="yellow",command=display)
button.place(x=7,y=9)
window.mainloop()