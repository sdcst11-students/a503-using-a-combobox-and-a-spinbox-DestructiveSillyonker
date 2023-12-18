# Retrieving values from a combobox
# Once a combobox is defined, how do you access the selected value?

import tkinter
from tkinter import ttk
import random

win = tkinter.Tk()
win.attributes('-topmost',True)

nF = tkinter.Frame(win)
l1 = tkinter.Label(nF,text="Roll a ")
c1 = ttk.Combobox(nF,values=[4,6,8,10,12,20,100],width=3,justify='center')
c1.set(6)
l2 = tkinter.Label(nF,text="sided die.")
b = tkinter.Button(win,text="Click to roll")
result =tkinter.Entry(win,text="roll result",justify="center")


nF.pack()
l1.pack(side=tkinter.LEFT)
c1.pack(side=tkinter.LEFT)
l2.pack(side=tkinter.LEFT)

b.pack()
result.pack()

def rollResult(event):
    print(event)
    data = c1.get()
    print(f"data contains:[{data}] that is type [{type(data)}]")

    value = int(data)
    roll = random.randint(1,value)
    result.delete(0,tkinter.END)
    result.insert(0,f"You rolled a {roll}")


b.bind("<Button>",rollResult)

win.mainloop()

"""
Code Analysis

line 28: Callback function to be run when there is a button event
line 30: Retrieve the current value of the combobox that is displayed
line 31: This is a debugging line to help us see the data that is collected
line 35-36:  Delete the previous entry box contents and put in new data

line 39: Bind a callback function to when the button "b" is clicked


reference:
https://docs.python.org/3/library/tkinter.ttk.html#combobox

"""
