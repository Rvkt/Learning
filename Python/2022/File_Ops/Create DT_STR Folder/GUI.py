import tkinter as tk
from tkinter import filedialog
from tkinter import *
from datetime import datetime
import os

root = Tk()
root.configure(bg='#111C26')
root.attributes('-topmost', True)

now = datetime.now()
dt_str = now.strftime('%Y%m%d')

def srcpath():
    global src
    src = filedialog.askdirectory()
def dir():
    for i in os.listdir(src):
        print(i)
def create():
    os.chdir(src)
    if not os.path.exists(dt_str):
        os.mkdir(dt_str)
    else:
        print(f'{dt_str} already exists in {src}')



create = Button(root, text='CREATE', padx=10, pady=5, fg='#111c26', bg='#f2b84b', command=create)
create.grid(row='1', column='2')

src = Button(root, text='SRC', padx=10, pady=5, fg='#111c26', bg='#f2b84b', command=srcpath)
src.grid(row='1', column='0')

files = Button(root, text='Files in SRC', padx=10, pady=5, fg='#111c26', bg='#f2b84b', command=dir)
files.grid(row='1', column='1')
root.mainloop()