from tkinter import *

root = Tk()
root.geometry('300x300')
root.title('Sliders')

vertical = Scale(root, from_=0, to=200)
vertical.pack()

horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack()

root.mainloop()
