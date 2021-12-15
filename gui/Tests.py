# encoding:utf-8
# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import *
from tkinter.ttk import *

master = Tk()
master.geometry("200x200")

def openNewWindow():
    
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(master)
    newWindow.title("New Window")

    # sets the geometry of toplevel
    newWindow.geometry("200x200")

    # A Label widget to show in toplevel
    Label(newWindow, text ="This is a new window").pack()


label = Label(master, text ="This is the main window")
label.pack(pady = 10)

# a button widget which will open a
# new window on button click
btn = Button(master,
            text ="Click to open a new window",
            command = openNewWindow)
btn.pack(pady = 10)

# mainloop, runs infinitely
mainloop()
