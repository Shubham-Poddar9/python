from tkinter import *
from PIL import Image,ImageTk
window=Tk()
window.title("Codingal")
window.geometry("400x400")
a=Image.open("HMMMMMMMMM.jpg")
b=ImageTk.PhotoImage(a)
label=Label(image=b,height=400,width=300)
label.place(x=6,y=7)
window.mainloop()