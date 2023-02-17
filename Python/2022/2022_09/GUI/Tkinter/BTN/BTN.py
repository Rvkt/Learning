from tkinter import *

root = Tk()
root = Tk(className="btn")  # pointing root to Tk() to use it as Tk() in program.
# root.withdraw()  # Hides small tkinter window.
root.geometry('200x200')
root.configure(bg='#F2F0F0')
root.attributes('-topmost', True)  # Opened windows will be active. above all windows despite selection.

path = Button(root, text="PATH", padx=10, pady=5, fg='#F26B83', bg='#203140', state=NORMAL)
path.pack()

path = Button(root, text="PATH", padx=10, pady=5, fg='#E6CC5C', bg='#203140', state=NORMAL)
path.pack()

path = Button(root, text="PATH", padx=10, pady=5, fg='#73FFF6', bg='#203140', state=NORMAL)
path.pack()

path = Button(root, text="PATH", padx=10, pady=5, fg='#F6FF73', bg='#203140', state=NORMAL)
path.pack()

root.mainloop()
