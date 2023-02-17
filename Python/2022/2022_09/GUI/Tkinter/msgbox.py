from tkinter import *
from tkinter import messagebox


root = Tk()
root.geometry('300x300')

# Information message box
def popup():
    messagebox.showinfo('Information Box', 'This is an example of\nInformation box')

# Warning message boxes
def popup1():
    messagebox.showwarning('Warning Box', 'This is an example of\nInformation box')
def popup2():
    messagebox.showerror('Warning Box', 'This is an example of\nInformation box')


# Question message boxes
def popup3():
    messagebox.askquestion('Question Message Box', 'This is an example of\n Question Message Box')
def popup4():
    messagebox.askokcancel('Question Message Box', 'This is an example of\nQuestion Message Box')
def popup5():
    messagebox.askretrycancel('Question Message Box', 'This is an example of\nQuestion Message Box')
def popup6():
    messagebox.askyesno('Question Message Box', 'This is an example of\nQuestion Message Box')
def popup7():
    messagebox.askyesnocancel('Question Message Box', 'This is an example of\nQuestion Message Box')



btn = Button(root, text='Btn', command=popup)
btn.pack()

btn1 = Button(root, text='Btn1', command=popup1)
btn1.pack()

btn2 = Button(root, text='Btn2', command=popup2)
btn2.pack()

btn3 = Button(root, text='Btn3', command=popup3)
btn3.pack()

btn4 = Button(root, text='Btn4', command=popup4)
btn4.pack()

btn5 = Button(root, text='Btn5', command=popup5)
btn5.pack()

btn6 = Button(root, text='Btn6', command=popup6)
btn6.pack()

btn7 = Button(root, text='Btn7', command=popup7)
btn7.pack()


root.mainloop()

