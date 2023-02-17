from tkinter import *
from tkinter import ttk
import tkinter.font as font


root = Tk()
root.title('String To list')

f1 = font.Font(family='Roboto Condensed', size=16, weight='bold')
# f2 = font.Font(family='Varela Round', size=11, weight='bold')
# f3 = font.Font(family='Chathura', size=18, weight='bold')


frame = LabelFrame(root, text='Palindrome Generator', padx=30, pady=10, fg='#203140')
frame.pack(pady=10, padx=15)

e = Entry(frame, width=30, bg='#f2f2f2', borderwidth=1, font=f1)
e.grid(row=0, column=0)
e.get()
e.delete(0, END)

def palindrome():
    global label
    txt1 = e.get()
    txt2 = txt1[-2::-1]
    join_txt = (txt1, txt2)
    join_txt = ''.join(join_txt)
    label.config(text=e.get())
    e.delete(0, END)


submit = Button(frame, text='Submit', font=f1, fg='#F6FF73', bg='#203140', width=15, state=NORMAL, command=palindrome, relief='raise')
submit.grid(row=0, column=2)

label = Label(frame, text='', font=f1, width=45, height=1, bg='#203140')
label.grid(row=1, column=0, columnspan=3, pady=10)

root.mainloop()