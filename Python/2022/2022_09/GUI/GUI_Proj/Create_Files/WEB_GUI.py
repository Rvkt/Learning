from tkinter import *
from tkinter import filedialog
import os

gui = Tk()
gui.title('Create Web Files')  # pointing frame to Tk() to use it as Tk() in program.
gui.configure(bg='#F2F0F0')
gui.attributes('-topmost', True)  # Opened windows will be active. above all windows despite selection.

# Functions

def browse():
    global path
    path = filedialog.askdirectory()
    os.chdir(path)
    path_label.config(text=path)

def create():
    global project
    try:
        if not os.path.exists(project):
            print(f'{project} is created in the {project.get()}.')
            os.mkdir(project)
    except:
        print('Already Exists!!')

os.chdir(path)

dict = {project: ['html', 'css', 'js']}
    for project in dict.projects():
        for value in (dict.get(project)):
            # print(f'{project}.{value}')
            with open(f'{project}.{value}', 'w'):
                print(f'{project}.{value} is Created.')
                pass

# GUI CODE
frame = Frame(gui,)
frame.pack(padx=40, pady=40)

path_label = Label(frame, text='Destination Path', fg='#F6FF73', bg='#203140')
path_label.grid(row=0, column=0)

browse_Btn = Button(frame, text="SRC", fg='#73FFF6', bg='#203140', state=NORMAL, command=browse)
browse_Btn.grid(row=0, column=1)

project = Entry(frame, text='Project Name')
project.grid(row=1, column=0)

create_Btn = Button(frame, text="Create", fg='#F6FF73', bg='#203140', state=NORMAL, command=create)
create_Btn.grid(row=1, column=1)

gui.mainloop()