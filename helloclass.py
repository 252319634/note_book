# -*- coding: utf-8 -*-
from Tkinter import *


class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()





























































        self.button = Button(frame, text='exit class', fg='red', command=frame.quit)
        self.button.pack()
        self.hibutton = Button(frame, text='say hi', fg='red', command=self.say_hi)
        self.hibutton.pack()

    def say_hi(self):
        print 'hi xp,thanks!'


root = Tk()
app = App(root)
root.mainloop()
# root.destroy()