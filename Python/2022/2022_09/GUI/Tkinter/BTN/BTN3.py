from tkinter import *
import tkinter.font as font
import crtfile, os


gui = Tk()  
gui.geometry('300x300')  

f = font.Font(family='Roboto Condensed', size=20, weight='bold')


def two_func(*funcs):
    def two_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return two_func
def changeText():
    if(btn['text']=='Click Me'):
        btn['text']='Clicked'
    else:
        btn['text']='Click Me'
def changeColor():
    if (btn['bg']) == 'green':
        btn['bg'] = 'red'
    else:
        btn['bg'] = 'green'


e = Entry(gui, width=25, bg='#f2f2f2', borderwidth=2)
e.grid(row=0, column=0, columnspan=3)
e.get()

def entry():
    greet = f'{e.get()}'
    print(greet)
    # label = Label(gui, text=greet)
    # label.grid(row=1, column=0, columnspan=3)


btn = Button(gui, text = "Click Me", bg="green", command = two_func(changeText, changeColor, entry))
btn['font'] = f
btn.grid(row=2, column=0, columnspan=3)
gui.mainloop()
