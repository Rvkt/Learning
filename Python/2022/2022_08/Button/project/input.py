from cgitb import text
import tkinter as tk
from tkinter import *

root = Tk()

def click():
    label= Label(root, text='button clicked')
    label.pack()
   

Button = Button(root, text='Button', command=click)
Button.pack()

root.mainloop()