from tkinter import *
from tkinter import filedialog as fd
from PIL import ImageTk, Image
import os

root = Tk()
root.geometry('250x100')
root.title('Open Image')


# root.filename = fd.askopenfile(initialdir= os.getcwd(),
# title='Select a file', filetypes=(('png files', '*.png'), ('All files', '*.*')))

# label = Label(root, text=root.filename).pack()

# myImg = ImageTk.PhotoImage(Image.open(root.filename))

# myImg_label = Label(image=myImg).pack()





def open():
    global myImg
    global label
    global myImg_label

    root.filename = fd.askopenfile(initialdir='os.getcwd()',
    title='Select a file', filetypes=(('png files', '*.png'), ('All files', '*.*')))
    label = Label(root, text=root.filename).pack()
    myImg = ImageTk.PhotoImage(Image.open(root.filename))
    myImg_label = Label(image=myImg).pack()


btn = Button(root, text='Open', command=open)        
btn.pack()


root.mainloop()
