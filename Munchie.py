# Author : Orion Ford (Credits go to : Micah Elias Ford (MY SON))
# Software: 202020V textMAIL


import tkinter as tk
from tkinter import *

root = Tk()
root.title('VISION txtMail v: 1.0')
root.geometry('700x400')


# popup window needed for prompt in future build.


# The Textbox w/
text1 = tk.Text(root, height=700, width=400)
text1.insert(tk.INSERT, "WELCOME TO VISION txtMAIL 1.0\n")
text1.insert(tk.INSERT, "Created by: DesignIsOrion\n")
text1.insert(tk.INSERT, "DELETE THIS MESSAGE TO BEGIN.\n")
text1.pack()


# Created by DesignIsOrion

# The Menubar
menubar = Menu(root)
root.config(menu=menubar)
filemenu = Menu(menubar, tearoff=0)

# Create file Menu In Menu Bar
menubar.add_cascade(label="File", menu=filemenu)

# Create file Menu In Menu Bar
filemenu.add_command(label="New", command=None)

# Create file Open In Menu Bar
filemenu.add_command(label="Open", command=None)

# Create file Save In Menu Bar
filemenu.add_command(label="Save", command=None)

# Create file Save As In Menu Bar
filemenu.add_command(label="Save As", command=None)

# SPACE
filemenu.add_command(label=" ", command=None)

# Create file About In Menu Bar
filemenu.add_command(label="About", command=None)

# Create file Save In Menu Bar
filemenu.add_command(label="Exit", command=None)


# Email Menu
menubar.add_cascade(label="Email Now")


# Chat Menu
menubar.add_cascade(label="VISION Connect")


root.mainloop()
