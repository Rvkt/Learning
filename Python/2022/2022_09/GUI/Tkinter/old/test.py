from tkinter import *
import os
from datetime import datetime
from tkinter import filedialog

root = Tk(className="mkdir")  # pointing root to Tk() to use it as Tk() in program.
root.withdraw()  # Hides small tkinter window.
root.geometry('300x100')
root.configure(bg='#111C26')
root.attributes('-topmost', True)  # Opened windows will be active. above all windows despite selection.
open_file = filedialog.askdirectory()  # Returns opened path as str
# print(open_file)
# print(os.listdir(open_file))
now = datetime.now()
dt_str = now.strftime('%Y%m%d%H%M')


# os.makedirs(path, exist_ok=True)
def mkdir():
    for d in open_file:
        try:
            os.makedirs(dt_str)
        except FileExistsError:
            pass


execute = Button(root, text="Execute", padx=10, pady=5, command=mkdir, fg='#111C26', bg='#F2B84B', command=mkdir)
execute.pack()

root.mainloop()
