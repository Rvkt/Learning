from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image Viewer')
root.geometry('200x230')

img01 = ImageTk.PhotoImage(Image.open('IMG01.png'))
img02 = ImageTk.PhotoImage(Image.open('IMG02.png'))
img03 = ImageTk.PhotoImage(Image.open('IMG03.png'))
img04 = ImageTk.PhotoImage(Image.open('IMG04.png'))
img05 = ImageTk.PhotoImage(Image.open('IMG05.png'))

img_list = [img01, img02, img03, img04, img05]

my_label = Label(image=img01)
my_label.grid(row=0, column=0, columnspan=3)

def right(image_number):
    global my_label
    global button_left
    global button_right

    my_label.grid_forget()
    my_label = Label(image=img_list[image_number-1])
    button_right = Button(root, text='>>', command=lambda: right(image_number+1))
    button_left = Button(root, text='<<', command=lambda:left(image_number-1))
    
    if image_number == 5:
        button_right = Button(root, text='>>', state=DISABLED)
    
    my_label.grid(row=0, column=0, columnspan=3)
    button_right.grid(row=1, column=2)
    button_left.grid(row=1, column=0)

def left(image_number):
    global my_label
    global button_left
    global button_right

    my_label.grid_forget()
    my_label = Label(image=img_list[image_number-1])
    button_right = Button(root, text='>>', command=lambda: right(image_number+1))
    button_left = Button(root, text='<<', command=lambda:left(image_number-1))

    if image_number == 1:
        button_left = Button(root, text='<<', state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_right.grid(row=1, column=2)
    button_left.grid(row=1, column=0)

button_left = Button(root, text='<<', command=left, state=DISABLED)
button_left.grid(row=1, column=0)

button_exit = Button(root, text='EXIT', command=root.quit)
button_exit.grid(row=1, column=1)

button_right = Button(root, text='>>', command=lambda: right(2))
button_right.grid(row=1, column=2)

root.mainloop()