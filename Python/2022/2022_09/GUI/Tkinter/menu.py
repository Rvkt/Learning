from tkinter import *
  
root = Tk()

def hello():
    print("hello world!")

# create a menu
menubar = Menu(root)
# create a sub-menu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=hello)
filemenu.add_command(label="Open", command=hello)
filemenu.add_command(label="Save", command=hello)

menubar.add_cascade(label="File", menu=filemenu)
menubar.add_command(label="Quit!", command=root.quit)

# display the menu
root.config(menu=menubar)
root.mainloop()