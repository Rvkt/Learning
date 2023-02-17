from tkinter import *
from tkinter import font

top = Tk()
L1 = Label(top, text="User Name")
L1.pack( side = LEFT)
E1 = Entry(top, bd =5, font=('Helvetica', 18, font.BOLD))
E1.pack(side = RIGHT)

top.mainloop()
