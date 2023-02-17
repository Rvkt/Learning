from tkinter import *
from tkinter import messagebox

tkWindow = Tk()
tkWindow.geometry('400x150')
tkWindow.title('Tkinter')


def showMsg():
    messagebox.showinfo('Message', 'Files are sorted!')


button = Button(tkWindow,
                text='Submit',
                command=showMsg)
button.pack()

tkWindow.mainloop()