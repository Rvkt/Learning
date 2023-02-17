from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry('300x300')
root.title('Images with tkinter')
root.iconbitmap('image.ico')


my_img = ImageTk.PhotoImage(Image.open('IMAGE.png'))
my_label = Label(image=my_img)
my_label.pack()


button_exit = Button(root, text='EXIT', command=root.quit)
button_exit.pack()


root.mainloop()