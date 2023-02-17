from tkinter import filedialog
from tkinter import *
from datetime import datetime
import os

root = Tk()
# root.withdraw()
root.configure(bg='#111C26')
root.attributes('-topmost', True)

now = datetime.now()
dt_str = now.strftime('%Y%m%d')
ft = ('Teko Bold', 20)
def global_browse():
    global path
    path = filedialog.askdirectory()
    os.chdir(path)


def Create():
    if not os.path.exists(dt_str):
        os.makedirs(os.path.join(dt_str), exist_ok=True)

# This select The Path.
browse = Button(root, text='BROWSE', padx=10, pady=5, fg='#111c26', bg='#f2b84b', font=ft,command=global_browse)
browse.pack()


# This creates the folder in the selected path.
Create = Button(root, text=f'Create {dt_str}', padx=10, pady=5, fg='#111c26', bg='#f2b84b',font=ft, command=Create)
Create.pack()
root.mainloop()