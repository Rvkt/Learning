from tkinter import *
from tkinter import filedialog
import os

gui = Tk()
gui.title('Create Files')  # pointing frame to Tk() to use it as Tk() in program.
gui.configure(bg='#F2F0F0')
gui.attributes('-topmost', True)  # Opened windows will be active. above all windows despite selection.

def browse():
    path = filedialog.askdirectory()
    os.chdir(path)
    path_label.config(text=path)

frame = Frame(gui,)
frame.pack(padx=20, pady=20)

path_label = Label(frame, text='Destination Path', width=75, height=3, fg='#F6FF73', bg='#203140')
path_label.grid(row=0, column=0, columnspan=3, padx=20, pady=10)

DOCUMENT = Button(frame, text="DOCUMENT", width=20, fg='#F6FF73', bg='#203140', state=NORMAL)
DOCUMENT.grid(row=1, column=0, padx=20, pady=10)

path = Button(frame, text="EBOOK", width=20, fg='#F6FF73', bg='#203140', state=NORMAL)
path.grid(row=1, column=1 ,padx=20, pady=10)

path = Button(frame, text="FONTS", width=20, fg='#F6FF73', bg='#203140', state=NORMAL)
path.grid(row=1, column=2,padx=20, pady=10)


path = Button(frame, text="AUDIO", width=20, fg='#F26B83', bg='#203140', state=NORMAL)
path.grid(row=2, column=0, padx=20, pady=10)

path = Button(frame, text="VIDEO", width=20, fg='#E6CC5C', bg='#203140', state=NORMAL)
path.grid(row=2, column=1, padx=20, pady=10)

path = Button(frame, text="IMAGE", width=20,  fg='#73FFF6', bg='#203140', state=NORMAL)
path.grid(row=2, column=2, padx=20, pady=10)


path = Button(frame, text="ILLUSTRATOR", width=20,  fg='#73FFF6', bg='#203140', state=NORMAL)
path.grid(row=3, column=1, padx=20, pady=10)

path = Button(frame, text="PHOTOSHOP", width=20,  fg='#73FFF6', bg='#203140', state=NORMAL)
path.grid(row=3, column=0, padx=20, pady=10)

path = Button(frame, text="SKETCHUP", width=20,  fg='#73FFF6', bg='#203140', state=NORMAL)
path.grid(row=3, column=2, padx=20, pady=10)


path = Button(frame, text="WEBFILES", width=20, fg='#F26B83', bg='#203140', state=NORMAL)
path.grid(row=4, column=0, padx=20, pady=10)

path = Button(frame, text="DEVFILES", width=20, fg='#73FFF6', bg='#203140', state=NORMAL)
path.grid(row=4, column=1, padx=20, pady=10)

path = Button(frame, text="SRC", width=20, height=4,  fg='#73FFF6', bg='#203140', state=NORMAL)
path.grid(row=4, column=2, rowspan=2, padx=20, pady=10)


path = Button(frame, text="ARCHIVE", width=20,  fg='#73FFF6', bg='#203140', state=NORMAL)
path.grid(row=5, column=0, padx=20, pady=10)

path = Button(frame, text="INSTALLER", width=20,  fg='#73FFF6', bg='#203140', state=NORMAL)
path.grid(row=5, column=1, padx=20, pady=10)


gui.mainloop()



