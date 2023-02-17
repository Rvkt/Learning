from tkinter import *
  
gui = Tk() 
gui.geometry("150x150") 
  
menuBtn = Menubutton(gui, text = "Menu")    
    
menuBtn.menu = Menu(menuBtn)   
menuBtn["menu"] = menuBtn.menu   
  
v1 = IntVar() 
v2 = IntVar() 
v3 = IntVar() 
  
menuBtn.menu.add_checkbutton(label = "Copy", variable = v1)   
menuBtn.menu.add_checkbutton(label = "Paste", variable = v2) 
menuBtn.menu.add_checkbutton(label = "Close", variable = v3) 
    
menuBtn.pack()   
gui.mainloop()