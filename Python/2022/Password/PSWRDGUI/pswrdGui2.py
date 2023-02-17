from tkinter import *
from random import randint


window=Tk()
window.title("Password Generator")
window.geometry('400x400')

def generatePass():
	password.delete(0,END)
	length=int(answer.get())
	my_pass=''
	for x in range(length):
		my_pass+=chr(randint(33,126))

	password.insert(0,my_pass)

labelFrame=LabelFrame(window,text="How many characters do you want in your password?")
labelFrame.pack(padx=10,pady=10)

answer=Entry(labelFrame,width=10)
answer.pack(padx=5,pady=10)

password=Entry(window,text='')		#display password
password.pack(pady=10)

newFrame=Frame(window)
newFrame.pack(pady=10)

generateBtn=Button(newFrame,text="Generate ", command=generatePass)
generateBtn.grid(row=0,column=0,padx=10,pady=10)








window.mainloop()