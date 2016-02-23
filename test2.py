# -*- coding: utf-8 -*-
from Tkinter import *
import hashlib

root = Tk()

text = Text(root, width=20, height=5)
text.pack()

text.insert(INSERT, "I love FishC.com!")
contents = text.get(1.0, END)

sig = contents

def check():
    contents = text.get(1.0, END)
    if sig != contents:
        print("警报：内容发生变动！")
    else:
        print("风平浪静~")

Button(root, text="检查", command=check).pack()

mainloop()