# -*- coding: utf-8 -*-
# 查找方法实例
from Tkinter import *
text = Text()
text.insert(END, "hello, world")

start = 1.0
while 1:
    pos = text.search("o", start, stopindex=END)
    if not pos:
        break
    print pos
    start = pos + "+1c"

