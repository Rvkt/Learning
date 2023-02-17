# Import the required libraries
from tkinter import *
from tkinter import ttk


# Create an instance of tkinter frame
win = Tk()


# Set the size of the tkinter window
win.geometry("700x350")


# Define the style for combobox widget
style = ttk.Style()
style.theme_use('xpnative')


# Define an event to close the window
def close_win(e):
   win.destroy()


# Add a label widget
label = ttk.Label(win, text="Eat, Sleep, Code and Repeat", font=('Times New Roman italic', 18), background="black", foreground="white")
label.place(relx=.5, rely=.5, anchor=CENTER)
ttk.Label(win, text="Now Press the ESC Key to close this window", font=('Aerial 11')).pack(pady=10)


# Bind the ESC key with the callback function
win.bind('<Escape>', lambda e: close_win(e))
win.mainloop()
