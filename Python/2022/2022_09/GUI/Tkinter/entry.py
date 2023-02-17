import tkinter as tk
from tkinter import *
from tkinter import filedialog

root = Tk(className="btn")  # pointing root to Tk() to use it as Tk() in program.
# root.withdraw()  # Hides small tkinter window.
root.geometry('200x200')
root.configure(bg='#F2F0F0')
root.attributes('-topmost', True)  # Opened windows will be active. above all windows despite selection.

e = Entry(root, width=25, bg='#f2f2f2', borderwidth=2)
e.pack()
e.get()
# e.insert(0, 'Enter Your Name: ')


def entry():
    greet = f'Hello, {e.get()}'
    label = Label(root, text=greet)
    label.pack()


path = Button(root, text="Submit", padx=20, pady=5, fg='#F6FF73', bg='#203140', state=tk.NORMAL, command=entry)
path.pack()

root.mainloop()
