import tkinter as tk
from tkinter import ttk

window = tk.Tk()

entry = tk.Entry(
    fg="red",
    bg="grey",
    width=30,
)
entry.pack()

label = tk.Label(
    text="Label",
    foreground="white",  # Set the text color to white
    background="black",  # Set the background color to black
    width=25,
    height=5
)
label.pack()

button = tk.Button(
    text="Button",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
button.pack()

window.mainloop()
