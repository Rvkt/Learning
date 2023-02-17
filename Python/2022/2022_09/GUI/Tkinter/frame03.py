# Import the required libraries
from tkinter import *

# Create an instance of tkinter frame
win= Tk()

# Define the size of the window
win.geometry("400x100")

# Define a function
def exit_win():
   win.destroy()

# Define a frame
button_container=Frame(win, relief="sunken", borderwidth=2)
button_container.pack(side="left", fill="x")

side_container=Frame(win, relief="sunken", borderwidth=2)
side_container.pack(side="left", fill= "y")

# Add widgets in frames
exit_btn=Button(button_container, text="Cancel", command=exit_win)
exit_btn.pack(side="left", padx= 10)
save_btn=Button(button_container, text="Save")
save_btn.pack(side="left", padx=10)

# Add a label widget in side_container frame
txt_label=Label(side_container, text="Tkinter is a Python Library", font=('Helvetica 15 bold'))

txt_label.pack(side= "right", padx=10)

win.mainloop()