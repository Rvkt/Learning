import tkinter as tk
from tkinter import *
from tkinter import filedialog

root = Tk(className="btn")
# root.geometry('400x400')
root.configure(bg='#F2F0F0')
root.attributes('-topmost', True)


frame = Frame(root, padx='30', pady='30')
frame.pack()

path_label = Label(frame, text='Path: ', width=10, bg='red')
path_label.grid(row=0, column=0, pady='10', padx='20')
path_entry = Entry(frame, width=25, bg='#f2f2f2', borderwidth=2)
path_entry.grid(row=0, column=1)
path_entry.get()


year_label = Label(frame, text='Year: ', width=10, bg='red')
year_label.grid(row=1, column=0, pady='10', padx='20')
year_entry = Entry(frame, width=25, bg='#f2f2f2', borderwidth=2)
year_entry.grid(row=1, column=1)
year_entry.get()


month_label = Label(frame, text='Month: ', width=10, bg='red')
month_label.grid(row=2, column=0, pady='10', padx='20')
month_entry = Entry(frame, width=25, bg='#f2f2f2', borderwidth=2)
month_entry.grid(row=2, column=1)
month_entry.get()

button = Button(frame, text='Create', width=40, bg='green')
button.grid(row='3', column='0', columnspan='2', pady='10', padx='20')




root.mainloop()