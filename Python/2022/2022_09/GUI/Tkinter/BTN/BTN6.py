from tkinter import filedialog
from tkinter import *
from datetime import datetime
import os

root = Tk()
# root.withdraw()
root.configure(bg='#111C26')
root.attributes('-topmost', True)

now = datetime.now()
dt_str = now.strftime('%Y%m%d%H%M')

def global_browse():
    path = filedialog.askdirectory()
    os.chdir(path)

def Create():
    os.makedirs(os.path.join(dt_str, 'path'), exist_ok=True)

# This select The Path.
browse = Button(root, text='BROWSE', padx=10, pady=5, fg='#111c26', bg='#f2b84b', command=global_browse)
browse.pack()

# This creates the folder in the selected path.
Create = Button(root, text='CREATE', padx=10, pady=5, fg='#111c26', bg='#f2b84b', command=Create)
Create.pack()
root.mainloop()