import tkinter as tk
from tkinter import *
from tkinter import filedialog

root = Tk(className="btn")  # pointing root to Tk() to use it as Tk() in program.
# root.withdraw()  # Hides small tkinter window.
# root.geometry('300x100')
root.configure(bg='#111C26')
root.attributes('-topmost', True)  # Opened windows will be active. above all windows despite selection.


def dstn():
    filedialog.askdirectory()


path = Button(root, text="PATH", padx=10, pady=5, fg='#111C26', bg='#F2B84B', command=dstn, state=tk.NORMAL)
path.pack()

execute = Button(root, text="EXECUTE", padx=10, pady=5, fg='#111C26', bg='#F2B84B')
execute.pack()

root.mainloop()
