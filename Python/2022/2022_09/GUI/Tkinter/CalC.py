from cgitb import text
from tkinter import *
root = Tk()
root.title("Calculator")

e = Entry(root, width=60, borderwidth=3)
e.grid(row=0, column=0, columnspan=4)



def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == 'addition':
        e.insert(0, f_num + int(second_number))

    if math == 'division':
        e.insert(0, f_num / int(second_number))

    if math == 'subtraction':
        e.insert(0, f_num - int(second_number))

    if math == 'multiplication':
        e.insert(0, f_num * int(second_number))




def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = 'division'
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(first_number)
    e.delete(0, END)



# Define Buttons
Btn_1 = Button(root, text='1',padx=40, pady=20, command=lambda:button_click(1))
Btn_2 = Button(root, text='2',padx=40, pady=20, command=lambda:button_click(2))
Btn_4 = Button(root, text='4',padx=40, pady=20, command=lambda:button_click(4))
Btn_3 = Button(root, text='3',padx=40, pady=20, command=lambda:button_click(3))
Btn_5 = Button(root, text='5',padx=40, pady=20, command=lambda:button_click(5))
Btn_6 = Button(root, text='6',padx=40, pady=20, command=lambda:button_click(6))
Btn_7 = Button(root, text='7',padx=40, pady=20, command=lambda:button_click(7))
Btn_8 = Button(root, text='8',padx=40, pady=20, command=lambda:button_click(8))
Btn_9 = Button(root, text='9',padx=40, pady=20, command=lambda:button_click(9))
Btn_0 = Button(root, text='0',padx=40, pady=20, command=lambda:button_click(0))
Btn_negate = Button(root, text='-',padx=40, pady=20, command=lambda: button_click())
Btn_decimal = Button(root, text='.',padx=40, pady=20, command=lambda: button_click())


Btn_divide = Button(root, text='/', padx=39, pady=20, command=lambda: button_divide())
Btn_multiply = Button(root, text='*', padx=39, pady=20, command=lambda: button_multiply())
Btn_subtract = Button(root, text='-', padx=39, pady=20, command=lambda: button_subtract())
Btn_add = Button(root, text='+', padx=39, pady=20, command=lambda:button_add())
Btn_equal = Button(root, text='=', padx=82, pady=20, command=button_equal)
Btn_clear = Button(root, text='Clr', padx=82, pady=20, command=lambda:button_clear())



Btn_1.grid(row=3, column=0)
Btn_2.grid(row=3, column=1)
Btn_3.grid(row=3, column=2)

Btn_4.grid(row=2, column=0)
Btn_5.grid(row=2, column=1)
Btn_6.grid(row=2, column=2)

Btn_7.grid(row=1, column=0)
Btn_9.grid(row=1, column=2)
Btn_8.grid(row=1, column=1)

Btn_0.grid(row=4, column=1)
Btn_negate.grid(row=4, column=0)
Btn_decimal.grid(row=4, column=2)


Btn_add.grid(row=1, column=3)
Btn_subtract.grid(row=2, column=3)
Btn_divide.grid(row=3, column=3)
Btn_multiply.grid(row=4, column=3)
Btn_equal.grid(row=5, column=2, columnspan=2)
Btn_clear.grid(row=5, column=0, columnspan=2)




root.mainloop()
