from tkinter import *

root = Tk()
root.title('Frame')
# root.geometry('300x300')

frame1 = LabelFrame(root, padx=50, pady=50)
frame1.pack(padx=10, pady=10)  # Padding works like margin.

btn1 = Button(frame1, text='Button 1')
btn1.grid(row=0, column=0)

btn2 = Button(frame1, text='Button 2')
btn2.grid(row=1, column=1)


root.mainloop()
