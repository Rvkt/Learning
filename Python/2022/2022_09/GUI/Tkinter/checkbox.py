from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry('300x300')
root.title('Checkbox')


Var = IntVar()
Var1 = StringVar()
C1 = Checkbutton(root, text = "Music", variable = Var, onvalue = 1, offvalue = 0, height=1, width = 20)
C1.pack()


C2 = Checkbutton(root, text = "String", variable = Var1, onvalue = 'ON', offvalue = 'OFF', height=1, width = 20)
C2.deselect()
C2.pack()


def slide():
    myLabel = Label(root, text=Var.get())
    myLabel.pack()

def slide1():
    myLabel = Label(root, text=Var1.get())
    myLabel.pack()


btn = Button(root, text='Show selection', command=slide)
btn.pack()


btn1 = Button(root, text='Show selection', command=slide1)
btn1.pack()


root.mainloop()