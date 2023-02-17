from tkinter import *
import tkinter.font as font


root = Tk()
root.title('Palindrome Generator')


f = font.Font(family='Roboto Condensed', size=12, weight='bold')


frame = LabelFrame(root, text='Palindrome Generator', padx=30, pady=5, fg='#203140')
frame.grid(row=0, column=0, columnspan=2, padx=30, pady=30)


txt = Entry(frame, width=27, bg='#f2f2f2', borderwidth=2, font=('Roboto Condensed', 18, font.BOLD))
txt.grid(row=0, column=0)
txt.get()


def palindrome(e):
    txt1 = txt.get()
    txt2 = txt1[-2::-1]
    join_txt = (txt1, txt2)
    join_txt = ''.join(join_txt)
    label = Label(frame, text=join_txt, padx=20, pady=20, fg='#203140',
    font=('Roboto Condensed', 18, font.BOLD))
    label.grid(row = 1, column = 0, columnspan = 3)
    txt.delete(0, END)


txt.bind('<Return>', palindrome)


root.mainloop()
