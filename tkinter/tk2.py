from tkinter import*
window=Tk()
window.title("Codingal")
window.geometry("550x550")
for i in range(3):
    for j in range(3):
        a=Frame(master=window,bg="green",relief=RAISED,borderwidth=3)
        a.grid(row=i,column=j,padx=20,pady=20)
        b=Label(master=a,text=f"{i}{j}")
        b.pack()
window.mainloop()