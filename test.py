# -*- coding: utf-8 -*-


from Tkinter import *

def app_text():
        text = e2.get()
        e1.insert(END, text)

def ins_text():
        text = e2.get()
        e1.insert(0, text)

def clr_text():
        e1.delete(0, END)

root = Tk()

e1 = Entry()
e2 = Entry()
b1 = Button(text = "Append Text", command = app_text)
b2 = Button(text = "Insert Text", command = ins_text)
b3 = Button(text = "Clear Text", command = clr_text)

e1.pack(padx = 10, pady = 10, fill = X)
e2.pack(padx = 10, pady = 10, fill = X)
b1.pack(padx = 10, pady = 5)
b2.pack(padx = 10, pady = 5)
b3.pack(padx = 10, pady = 5)

root.mainloop()