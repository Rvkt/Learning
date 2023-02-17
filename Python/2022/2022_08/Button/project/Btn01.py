from cProfile import label
from tkinter import *

root = Tk()


e = Entry(root, )
e.pack()
e.get()

def greet():
    Label2= Label(root, text=f'Hello, {eget}')
    Label2.pack()

btn02= Button(root, text='Button2', command=greet)
btn02.pack()


def click():
    label= Label(root, text='button clicked')
    label.pack()
   

Button = Button(root, text='Button', command=click)
Button.pack()

root.mainloop()