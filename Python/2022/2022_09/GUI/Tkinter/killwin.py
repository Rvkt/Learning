from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("300x180")
root.title('Base Window')

def open_root():
   new = Toplevel(root)
   new.geometry("300x180")
   new.title("WinTwo")
   Label(new, text="Hey, Howdy?\n This is second window.", font=('Helvetica 12 bold')).pack(pady=30)
   btn = Button(new, text='Close', command=new.destroy)
   btn.pack()



Label(root, text= "Click the button to\nOpen a New Window", font= ('Helvetica 12 bold')).pack(pady=30)

ttk.Button(root, text="Open", command=open_root).pack()
root.mainloop()



root.mainloop()