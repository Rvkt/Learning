from tkinter import *

root = Tk(className="Sorter")
root.geometry('300x100')
root.configure(bg='#111C26')


execute = Button(root, text="Execute", padx=10, pady=5, command=sort, fg='#111C26', bg='#F2B84B')
execute.pack()


root.mainloop()

