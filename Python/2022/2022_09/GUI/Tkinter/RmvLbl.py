from tkinter import *

root = Tk()


def remove():
    hello = 'hello ', e.get()
    myLabel = Label(root, text=hello)
    e.delete(0, END)
    myLabel.pack(pady=10)


e = Entry(root, width=50, font=('Helvetica', 30))
e.pack(padx=10, pady=10)


btn = Button(root, text='Name Please', command=remove) 
btn.pack(pady=10)


root.mainloop()