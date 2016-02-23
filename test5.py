# -*- coding: utf-8 -*-
# tag_config：创建一个指定背景颜色的 TAG
from Tkinter import *

root = Tk()
t = Text(root)
# 创建一个 TAG，其前景色为红色
t.tag_config('a', foreground='white', background='blue')
# 使用 TAG 'a'来指定文本属性
t.insert(1.0, '0123456789')
t.tag_add('a','1.0')
t.pack()
root.mainloop()
# 结果是文本颜色改变为红色了