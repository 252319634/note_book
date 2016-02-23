__author__ = 'Sundy'

from Tkinter import *
import tkMessageBox

root = Tk()

def callback():
    if tkMessageBox.showerror('Sundy','HI Sundy'):
        print 'Clciked Yes'
    else:
        print 'Clicked No'

button = Button(root, text='Button1', command=callback)
button.pack()
root.mainloop()