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
    path_label.config(text=path)


def Create():
    if not os.path.exists(dt_str):
        os.makedirs(os.path.join(dt_str), exist_ok=True)

# This select The Path.
browse = Button(root, text='BROWSE', width=20, padx=10, pady=5, fg='#111c26', bg='#f2b84b', command=global_browse)
browse.grid(row=0, column=1)

# Shows the path
path_label = Label(root, text='Choose Destination Directory', width=50, bg='#D3D3D3', pady=5, padx=10)
path_label.grid(row=0, column=0)

# This creates the folder in the selected path.
Create = Button(root, text='CREATE', width=75, padx=10, pady=5, fg='#111c26', bg='#f2b84b', command=Create)
Create.grid(row=2, column=0, columnspan=2)

root.mainloop()