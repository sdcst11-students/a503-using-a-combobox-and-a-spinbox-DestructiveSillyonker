# Basic definition of a combobox

import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.attributes('-topmost',True)

l1 = tkinter.Label(win,text="This is a sample of a combobox")
c1 = ttk.Combobox(win,values=["t1","t2"])
c1.set('t1')

l1.pack()
c1.pack()
win.mainloop()

"""
Code Analysis

line 4: imports the extra widgets from tkinter
line 7: allows you to add extra attributes. This one keeps the window pinned on top of other windows
line 10: creates a combobox with 2 options
line 11: sets the default value of the c1 combobox.
See the reference page for extra 

reference:
https://docs.python.org/3/library/tkinter.ttk.html#combobox

"""
