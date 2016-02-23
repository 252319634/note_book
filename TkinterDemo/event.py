__author__ = 'Sundy'

from Tkinter import *
import tkMessageBox

root = Tk()

def callback(event):
    frame.focus_set()
    print "clicked at:", event.x, event.y



def key(event):
    print "pressed", repr(event.char)

def closeWindow():
    if tkMessageBox.askokcancel('Quit',"Do you want to exit"):
        root.destroy()

frame = Frame(root,width=100,height=100)
frame.bind('<Button-1>',callback)
frame.bind('<Key>',key)
frame.pack()

root.protocol('WM_DELETE_WINDOW',closeWindow)

root.mainloop()