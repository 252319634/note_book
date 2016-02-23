__author__ = 'Sundy'

from Tkinter import *

class App:
    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text='Exit Class', fg='red', command=frame.quit)

        self.button.pack()

        self.hiButton = Button(frame, text='Say Hi', command=self.say_hi)
        self.hiButton.pack()

    def say_hi(self):
        print "Hi Sundy , Thanks!"

root = Tk()


root = Tk()
app = App(root)
root.mainloop()
#root.destroy()
