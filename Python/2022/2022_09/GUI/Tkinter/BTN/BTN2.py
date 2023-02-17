from tkinter import *
import tkinter.font as font
from tkinter import messagebox

gui = Tk()  
gui.geometry('300x300')  


# set the font.
f = font.Font(family='Roboto Condensed', size=20, weight='bold')


def changeText01():  
    btn01['text'] = 'Ipsum'

def changeText02():  
  if(btn02['text']=='Lorem'):
    btn02['text']='Ipsum'
  else:
    btn02['text']='Lorem'

def msgCallBack():
   messagebox.showinfo("StackHowTo", "Welcome to StackHowTo!")

def two_funcs(*funcs):
    def two_funcs(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return two_funcs
def changeText():  
    btn04['text'] = 'Welcome to StackHowTo!'
def changeColor():  
    btn04['bg'] = 'Red'


btn = Button(gui, text ="Msg Box", command = msgCallBack)
btn.grid(row=0, column=0) 

btn01 = Button(gui, text='Lorem', command=changeText01)  
btn01.grid(row=1, column=0)  
  
btn02 = Button(gui, text='Lorem', command=changeText02)  
btn02.grid(row=2, column=0) 

# create button
btn03 = Button(gui, text='Click here!', bg='#203140', fg='#F26B83')
# apply font to the button label
btn03['font'] = f
# add button to window
btn03.grid(row=3, column=0) 

btn04 = Button(gui, text = "Change text and color", command = two_funcs(changeText, changeColor))
btn04.grid(row=4, column=0)


gui.mainloop()





















  
