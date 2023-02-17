from tkinter import *
from tkinter import filedialog
from datetime import datetime
from datetime import datetime
from time import strftime, time
import os



q = Tk()
q.geometry('300x200')
q.title('Digital Clock')

e = Entry(q, text='', width=30, font=('Chathura ExtraBold', 20))
e.grid(row=2, column=0, columnspan=2)
e.get()


def date():

    global now;
    now = datetime.now()
    year_full = now.strftime('%Y')
    month_str = now.strftime('%b').upper()
    day_month = now.strftime('%d').zfill(2)
    day_name =  now.strftime('%a').upper()
    hour_24 =   now.strftime('%H').zfill(2)
    minutes =   now.strftime('%M').zfill(2)
    clock_str = f'{year_full} {month_str} {day_month} {day_name} {hour_24} {minutes}'
 
    rtclock.config(text=clock_str)
    rtclock.after(500, date)


def global_browse():
    path = filedialog.askdirectory()
    os.chdir(path)
    path_label.config(text=path)


def Create():
    if not os.path.exists(e.get()):
        os.makedirs(os.path.join(e.get()), exist_ok=True)


rtclock = Label(q, text='', fg='#0e1013', font=('Chathura ExtraBold', 20))
rtclock.grid(row=0, column=0, columnspan=2)


path_label = Label(q, text='Choose Destination Directory', bg='#D3D3D3', pady=5, padx=10)
path_label.grid(row=1, column=0)


browse = Button(q, text='BROWSE', padx=10, pady=5, fg='#111c26', bg='#f2b84b', command=global_browse)
browse.grid(row=1, column=1)

# entry here
Create = Button(q, text='CREATE', padx=10, pady=5, fg='#111c26', bg='#f2b84b', command=Create)
Create.grid(row=3, column=0, columnspan=2)

date()
q.mainloop()


'''
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
browse = Button(root, text='BROWSE', padx=10, pady=5, fg='#111c26', bg='#f2b84b', command=global_browse)
browse.grid(row=0, column=1)

# Shows the path
path_label = Label(root, text='Choose Destination Directory', bg='#D3D3D3', pady=5, padx=10)
path_label.grid(row=0, column=0)

# This creates the folder in the selected path.
Create = Button(root, text='CREATE', padx=10, pady=5, fg='#111c26', bg='#f2b84b', command=Create)
Create.grid(row=0, column=2)
root.mainloop()'''