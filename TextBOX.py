from tkinter import *
from tkinter import filedialog
from tkinter import filedialog
from tkinter import messagebox
import os

root =Tk()

root.title("Untitled - TextBox")
root.geometry("600x400")
root.resizable(True, True)

text = Text(root)

root.grid_rowconfigure(0,weight=1)
root.grid_columnconfigure(0,weight=1)

text.grid(sticky=N+E+S+W)

#Menu Function Define Start

#File Menu

def new(Event = None):
    root.title("Untitled - TextBox")
    text.delete('1.0', END)

def open(Event = None):
    files = filedialog.askopenfile(filetypes = (("Text files","*.txt"),("all files","*.*")), title = "Select a File")
    doc = files.name
    root.title(f"{os.path.basename(doc)} - TextBOX")
    text.insert(INSERT, files.read())

def save(Event = None):
    path = filedialog.asksaveasfile(mode = 'w', initialfile='Untitled.txt', defaultextension=".txt", filetypes = (("Text files","*.txt"),("all files","*.*")))
    forsave = str(text.get('1.0', END))
    path.write(forsave)
    path.close()
    root.title(f"{os.path.basename(path)} - TextBOX")

def exit():
    root.quit()

# Edit Menu

def undo():
    text.event_generate("<<Undo>>")

def redo():
    text.event_generate("<<Redo>>")

def cut():
    text.event_generate("<<Cut>>")

def copy():
    text.event_generate("<<Copy>>")

def paste():
    text.event_generate("<<Paste>>")

def clear():
    text.event_generate("<<Clear>>")

# About

def about_TextBOX():
    root1 = Tk()
	
    root1.title("About TextBOX")
    root1.maxsize(400, 340)
	
    lbl1 = Label(root1, text = "Developer : Rahul Dhar", font = ("Arial",15))
    lbl1.pack()
    lbl2 = Label(root1, text = "Written IN : Python 3.6", font = ("Arial",15))
    lbl2.pack()
    lbl3 = Label(root1, text = "Software Use : Visual Studio Code v1.28.2\nGit Bash", font = ("Arial",15))
    lbl3.pack()
	
    root1.mainloop()

def about_us():
    root2 = Tk()
	
    root2.title("About TextBOX")
    root2.maxsize(400, 340)
	
    lbl1 = Label(root2, text = "Developer : Rahul Dhar", font = ("Arial",15))
    lbl1.pack()
    lbl2 = Label(root2, text = "Email : rdhar8502@gmail.com", font = ("Arial",15))
    lbl2.pack()
    lbl3 = Label(root2, text = "Contact : +91 98753 97872", font = ("Arial",15))
    lbl3.pack()
	
    root2.mainloop()

#menu Start

menu = Menu(root)
root.config(menu = menu)

#submenu 1

submenu1 = Menu(menu)
menu.add_cascade(label = 'File', menu = submenu1)
submenu1.add_command(label = 'New', command = new)
submenu1.add_command(label = 'Open', command = open)
submenu1.add_command(label = 'Save', command = save)
submenu1.add_command(label = 'Exit', command = exit)

#submenu 2

submenu2 = Menu(menu)
menu.add_cascade(label = 'Edit', menu = submenu2)
submenu2.add_command(label = 'Undo', command = undo)
submenu2.add_command(label = 'Redo', command = redo)
submenu2.add_command(label = 'Cut', command = cut)
submenu2.add_command(label = 'Copy', command = copy)
submenu2.add_command(label = 'Paste', command = paste)
submenu2.add_command(label = 'Clear', command = clear)

#Submenu 3

submenu3 = Menu(menu)
menu.add_cascade(label = 'Help', menu = submenu3)
submenu3.add_command(label = 'About TextBOX', command = about_TextBOX)
submenu3.add_command(label = 'About Us', command = about_us)

#Menu End

# Save
root.bind("<Control - s>", save)
root.bind("<Control - S>", save)

# New
root.bind("<Control - N>", new)
root.bind("<Control - n>", new)

# Open
root.bind("<Control - o>", open)
root.bind("<Control - O>", open)



root.mainloop()