from tkinter import *
window=Tk()
window.title("codingal")
window.geometry("400x400")
window.configure(bg="yellow")
def display():
    a=Toplevel()
    a.configure(bg="green")
    a.title("color")
    a.geometry("200x200")
    a.mainloop()
button=Button(window,text="color",fg="black",bg="white",command=display)
button.place(x=3,y=5)
window.mainloop()