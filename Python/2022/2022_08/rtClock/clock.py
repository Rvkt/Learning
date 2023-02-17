from tkinter import *
from datetime import datetime
from time import strftime, time
from PIL import ImageTk,Image

q = Tk()
q.geometry('600x400')
# q.minsize(100,50)
q.title('Digital Clock')



def clock():
    global now;
    now = datetime.now()

    hour_24 =   now.strftime('%H').zfill(2)
    hour_12 =   now.strftime('%I').zfill(2)
    minutes =   now.strftime('%M').zfill(2)
    second =    now.strftime('%S').zfill(2)
    amPm =      now.strftime('%p').upper()





    clock_label.config(text=hour_24 + " " + minutes + " " + second)
    clock_label.after(250, clock)

def date():

    year_full = now.strftime('%Y')
    year_short = now.strftime('%y').zfill(2)
    month_str = now.strftime('%b').upper()
    month_int = now.strftime('%m').zfill(2)
    day_month = now.strftime('%d').zfill(2)
    day_year = now.strftime('%j').zfill(2)

    date_label.config(text=year_full + " " + month_str + " " + day_month)
    date_label.after(250, date)

clock_label = Label(q, text='', fg='red', font=('Teko Regular', 48))
clock_label.pack(pady=20)

date_label = Label(q, text='', fg='red', font=('Teko Regular', 48))
date_label.pack(pady=20)

lb01 = Label(q, text='', fg='red', bg='#0e1013', font=('Teko Regular', 48))
lb01.pack()

clock()
date()

'''f1 = Frame(q, width=750, height=200, bg='#0e1013')
f1.pack(expand=True)'''

q.mainloop()