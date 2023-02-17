from tkinter import filedialog
from tkinter import *
from datetime import datetime
import os

root = Tk()
# root.geometry('500x500')
root.title('Create Directory')
root.configure(bg='#111C26')
root.attributes('-topmost', True)

now = datetime.now()
dt_str = now.strftime('%Y%m%d')
f = font=('Chathura ExtraBold', 20)

def date():
    global now;
    now = datetime.now()

    year_full = now.strftime('%Y')
    month_str = now.strftime('%b').upper()
    day_month = now.strftime('%d').zfill(2)
    day_name =  now.strftime('%a').upper()
    hour_24 =   now.strftime('%I').zfill(2)
    minutes =   now.strftime('%M').zfill(2)
    second =    now.strftime('%S').zfill(2)
    amPm =      now.strftime('%p').upper()

    clock_str = f'{year_full} {month_str} {day_month} {day_name} {hour_24} {minutes} {second}' 

    rtclock.config(text=clock_str)
    rtclock.after(500, date)

def global_browse():
    path = filedialog.askdirectory()
    os.chdir(path)
    path_label.config(text=path)

def Create():
    if not os.path.exists(dt_str):
        os.makedirs(os.path.join(dt_str), exist_ok=True)

rtclock = Label(root, text='', fg='#f2b84b',bg='#111C26', font=f)
rtclock.pack()

frame = Frame(root,)
frame.pack()

browse = Button(frame, text='BROWSE', width=25, font=f, fg='#111c26', bg='#f2b84b', command=global_browse)
browse.grid(row=1, column=0)

path_label = Label(frame, text='Choose Destination Directory', width=50, height=2, font=f, bg='#D3D3D3')
path_label.grid(row=0, column=0, columnspan=2)

Create = Button(frame, text='CREATE', width=25, font=f, fg='#111c26', bg='#f2b84b', command=Create)
Create.grid(row=1, column=1)

date()
root.mainloop()