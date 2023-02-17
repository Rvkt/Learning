from tkinter import *
from datetime import datetime
from time import strftime, time

q = Tk()
q.geometry('500x100')
q.title('Digital Clock')

def date():
    global now;
    now = datetime.now()

    year_full = now.strftime('%Y')
    month_str = now.strftime('%b').upper()
    day_month = now.strftime('%d').zfill(2)
    day_name =  now.strftime('%a').upper()
    hour_24 =   now.strftime('%H').zfill(2)
    minutes =   now.strftime('%M').zfill(2)
    second =    now.strftime('%S').zfill(2)
    amPm =      now.strftime('%p').upper()

    clock_str = f'{year_full}{month_str}{day_month}{day_name}{hour_24}{minutes}{second}{amPm}' 

    rtclock.config(text=year_full
     + " " + 
     month_str
      + " " + 
      day_month
       + " " + 
       day_name
        + " " + 
        hour_24
         + " " +
         minutes)
    rtclock.after(500, date)

rtclock = Label(q, text='', fg='red',bg='#0e1013', pady='100', padx='500', font=('Chathura ExtraBold', 48))
rtclock.pack()

date()
q.mainloop()