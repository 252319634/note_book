__author__ = 'Sundy'

from Tkinter import *

root = Tk()

label = Label(root,text='Hello world')
label.config(cursor='gumby')
label.config(width=80,height=10,fg='yellow',bg='dark green')
label.config(font=('times','28','bold'))
label.pack()
root.mainloop()


