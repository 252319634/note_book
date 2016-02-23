__author__ = 'Sundy'

from Tkinter import *

root = Tk()

def callback():
    print "clicked tool bar button "

toolbar = Frame(root)
b = Button(toolbar,text='new',width=6,command=callback)
b.pack(side=LEFT,padx=2,pady=2)

c = Button(toolbar,text='open',width=6,command=callback)
c.pack(side=LEFT,padx=2,pady=2)

toolbar.pack(side=TOP,fill=X)
root.mainloop()

