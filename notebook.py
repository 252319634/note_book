# -*- coding: utf-8 -*-
# python 使用的是2.7.10 32位版本

from Tkinter import *
from tkMessageBox import *
from tkFileDialog import *
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

filename = ''  # 文件名
filecontent = ''  # 文件起始内容


def author():
    showinfo('作者信息', '本软件由麦子学院Sundy完成')


def about():
    showinfo('版权信息.Copyright', '本软件版权归属为麦子学院')


def get():
    # text.get()方法返回的文本内容最后面会加一个换行 \n 不知道为什么!
    # 去掉\n,才能与原文比较是否相同,否则的话刚读入文件就会被判断成已经修改过了.
    return textPad.get(1.0, END)[:-1]


def update(name, content):
    # 更新文件信息,使用全局变量保存文件的全路径和文件内容
    global filename, filecontent
    filename = name
    filecontent = content


def flag():
    # 这个函数用于判断更改
    # 文件修改标志,通过修改前后的内容对比得出结果 并返回,修改为True.
    msg = get()  # msg 后面会加一个换行 \n 不知道为什么!
    return not (msg == filecontent)  # 相等为没修改,所以加 not.


def asksave():
    # 是/否/取消 保存对话框
    if filename == '':  # 判断是不是新建的文件
        message = '是否保存文件:未命名文件'
    else:
        message = '是否保存文件:' + os.path.basename(filename)
    return askyesnocancel(title='文件已更改!', message=message)  # 弹出是否保存对话框,有三个按钮yes,no,cancel
    # ync 有三个返回值: 是:True,否:False,取消:None


def close():
    # 如果内容有修改 将提出保存更改
    if flag():  # 如果有改变
        ync = asksave()
        # ync 有三个返回值: 是:True,否:False,取消:None
        if ync == True:
            return save()
        if ync == False:  # 放弃保存
            v.set('不保存')
            return True
        else:  # 取消
            v.set('取消')
            return False
    else:  # 如果内容没有变化,不用关闭文件,直接返回True表示已经关闭完成
        if filename != '':
            v.set('内容没有修改,直接打开新文件!')
            return True
        else:
            return True


def new():
    if get() == '' and filename == '':
        v.set('已经是空文件,无需再次新建!')
    elif close():  # 先关闭之前的文件,再新建
        root.title('未命名文件')
        textPad.delete(1.0, END)  # 清空textpad内容
        textPad.edit_reset()  # 这句重置undo,redo 为空了.
        update('', '')  # 更新文件信息
        # v.set(u'新建 未命名文件')


def openfile():
    if close():  # 先成功关闭已经打开的文件
        v.set('请选择要打开的文件!')
        filename = askopenfilename(defaultextension='.txt')  # 获得对话框返回的文件名
        if filename == '':
            v.set('没有选择文件!')  # 如果没有返回文件名,就什么也不干
        else:  # 如果有返回文件名就修改标题,清空textpad,读取内容.
            root.title('FileName:' + os.path.basename(filename))
            with open(filename, 'r') as f:  # 打开文件
                msg = f.read()  # 读取文件
            textPad.delete(1.0, END)  # 清空记事本内容
            textPad.insert(1.0, msg)  # 文件内容写入记事本
            textPad.edit_reset()  # 这句重置undo,redo 为空了.
            update(filename, msg)
            v.set('成功打开文件:' + filename)
            return True


def save():
    if filename != '':  # 有文件路径,说明是打开的文件,就保存到原来的路径
        if flag():  # 如果有修改文件
            msg = get()
            with open(filename, 'w') as f:
                f.write(msg)
            update(filename, msg)
            v.set('成功保存文件:' + filename)
            return True
        else:
            v.set('无修改,不用保存!')
            return True
    else:  # 文件路径为空,说明是新建的文件,就执行saveas().
        return saveas()


def saveas():
    # 另存为处理
    # 得到一个新文件路径后保存文件
    v.set('请指定新文件名!')
    filename = asksaveasfilename(initialfile='未命名.txt', defaultextension='.txt')
    if filename:
        msg = get()
        with open(filename, 'w') as fh:
            fh.write(msg)
        update(filename, msg)
        v.set('成功保存文件:' + filename)
        root.title('FileName:' + os.path.basename(filename))
        return True
    else:
        v.set('已取消保存!')
        return False


def myquit():
    if close():
        quit()


def cut():
    textPad.event_generate('<<Cut>>')


def copy():
    textPad.event_generate('<<Copy>>')


def paste():
    textPad.event_generate('<<Paste>>')


def redo():
    textPad.event_generate('<<Redo>>')


def undo():
    textPad.event_generate('<<Undo>>')


def selectAll():
    textPad.tag_add('sel', '1.0', END)


keyword = ''  # 关键词
poss = []  # 找到的关键词位置列表
position = 0

# search 功能开始
def search(event):  # 没有找到让新窗口获得焦点的方法..
    def tag_end(a=0):
        # 计算tag的结束位置
        end = '%s+%sc' % (poss[position + a], str(len(keyword)))
        return end

    def tag_start(a=0):
        # 计算tag的起始位置
        return poss[position + a]

    def next():
        global poss, position
        if position < len(poss):
            # if position != 0:
            #     textPad.tag_remove('a', tag_start(-1), tag_end(-1))
            textPad.tag_add('a', tag_start(), tag_end())
            textPad.see(poss[position])
            v.set('找到%s个,第%s个' % ((len(poss)),position+1))
            position += 1
        else:
            textPad.tag_add('b', tag_start(-1), tag_end(-1))
            v.set('没了!')
            if askyesno(title='没有了', message='是否从头查找?'):
                search_clear()
                # entry1.focus_set()
                find1()
            entry1.focus_set()

    def search_clear():  # 如果关掉查询框,就重置查询状态.
        global keyword, poss, position
        keyword = ''
        poss = []
        position = 0
    def tag_clear():
        # 清除tag标记
        textPad.tag_remove('a', '1.0', 'end')

    search_clear()  # 一打开查找窗口就重置一下查询状态
    def find1():  # 查找并定位高亮关键字
        global keyword, poss, position
        tag_clear()
        start = 1.0
        kw = entry1.get()
        if keyword != kw:
            search_clear()  # 重置查找状态
            tag_clear()
            keyword = entry1.get()  # 更新关键词
            while 1:
                pos = textPad.search(keyword, start, stopindex=END)
                if not pos:
                    break
                poss.append(pos)
                start = pos + "+1c"
            if poss:
                v.set('找到%s个' % (len(poss)))
                next()
            else:
                v.set('没有找到!')
                search_clear()
        elif kw == '':
            v.set('请输入关键词')
        else:
            next()

    topsearch = Toplevel(root)
    # topsearch.protocol('WM_DELETE_WINDOW', search_clear)
    m_x = str(event.x_root - 150)
    m_y = str(event.y_root + 25)
    zuobiao = '300x30+' + m_x + '+' + m_y
    topsearch.geometry(zuobiao)
    label1 = Label(topsearch, text='查找内容:')
    label1.grid(row=0, column=0, padx=5)
    entry1 = Entry(topsearch, width=20)
    entry1.grid(row=0, column=1, padx=5)
    button1 = Button(topsearch, text='查找下一个', command=find1)
    button1.grid(row=0, column=2)
    entry1.focus_set()

# search 功能结束


root = Tk()
root.protocol('WM_DELETE_WINDOW', myquit)  # 主窗口退出事件将触发myquit
root.title('未命名文件')
root.geometry("800x500+100+100")

# Create Menu
menubar = Menu(root)
root.config(menu=menubar)

filemenu = Menu(menubar)
filemenu.add_command(label='新建', accelerator='Ctrl + N', command=new)
filemenu.add_command(label='打开', accelerator='Ctrl + O', command=openfile)
filemenu.add_command(label='保存', accelerator='Ctrl + S', command=save)
filemenu.add_command(label='另存为', accelerator='Ctrl + Shift + S', command=saveas)
filemenu.add_command(label='关闭', accelerator='Ctrl + Q', command=myquit)
menubar.add_cascade(label='文件', menu=filemenu)

editmenu = Menu(menubar)
editmenu.add_command(label='撤销', accelerator='Ctrl + Z', command=undo)
editmenu.add_command(label='重做', accelerator='Ctrl + y', command=redo)
editmenu.add_separator()
editmenu.add_command(label="剪切", accelerator="Ctrl + X", command=cut)
editmenu.add_command(label="复制", accelerator="Ctrl + C", command=copy)
editmenu.add_command(label="粘贴", accelerator="Ctrl + V", command=paste)
editmenu.add_separator()
editmenu.add_command(label="查找", accelerator="Ctrl + F", command=search)
editmenu.add_command(label="全选", accelerator="Ctrl + A", command=selectAll)
menubar.add_cascade(label="编辑", menu=editmenu)
aboutmenu = Menu(menubar)
aboutmenu.add_command(label="作者", command=author)
aboutmenu.add_command(label="版权", command=about)
menubar.add_cascade(label="关于", menu=aboutmenu)

# toolbar
toolbar = Frame(root, height=25, bg='light sea green')
shortButton = Button(toolbar, text='新建', command=new)
shortButton.pack(side=LEFT, padx=5, pady=5)
shortButton = Button(toolbar, text='打开', command=openfile)
shortButton.pack(side=LEFT, padx=5, pady=5)
shortButton = Button(toolbar, text='保存', command=save)
shortButton.pack(side=LEFT, padx=5, pady=5)
shortButton = Button(toolbar, text='另存', command=saveas)
shortButton.pack(side=LEFT, padx=5, pady=5)
shortButton = Button(toolbar, text='|', command='', bg='light sea green')
shortButton.pack(side=LEFT, padx=10, pady=5)

shortButton = Button(toolbar, text='撤销', command=undo)
shortButton.pack(side=LEFT, padx=5, pady=5)
shortButton = Button(toolbar, text='重做', command=redo)
shortButton.pack(side=LEFT, padx=5, pady=5)
shortButton = Button(toolbar, text='|', command='', bg='light sea green')
shortButton.pack(side=LEFT, padx=10, pady=5)

shortButton = Button(toolbar, text='剪切', command=cut)
shortButton.pack(side=LEFT, padx=5, pady=5)
shortButton = Button(toolbar, text='复制', command=copy)
shortButton.pack(side=LEFT, padx=5, pady=5)
shortButton = Button(toolbar, text='粘贴', command=paste)
shortButton.pack(side=LEFT, padx=5, pady=5)
shortButton = Button(toolbar, text='|', command='', bg='light sea green')
shortButton.pack(side=LEFT, padx=10, pady=5)

shortButton = Button(toolbar, text='查找')
shortButton.bind('<Button-1>', lambda event: search(event))
shortButton.pack(side=LEFT, padx=5, pady=5)
shortButton = Button(toolbar, text='全选', command=selectAll)
shortButton.pack(side=LEFT, padx=5, pady=5)

toolbar.pack(expand=NO, fill=X)

# 状态栏
v = StringVar()
v.set('新建 未命名文件')  # 初始状态显示这个
status = Label(root, bd=1, relief=SUNKEN, anchor=W, textvariable=v)
status.pack(side=BOTTOM, fill=X)

# linenumber&text
lnlabel = Label(root, width=2, bg='antique white')
lnlabel.pack(side=LEFT, fill=Y)

textPad = Text(root, undo=True, autoseparators=0, maxundo=1000)
textPad.tag_config('a', foreground='white', background='blue')
textPad.tag_config('b', foreground='black', background='white')
textPad.bind('<Key>', lambda event: textPad.edit_separator())
# 给撤销增加分隔符,每发生一次事件就添加一次分隔,可以使撤销以单次输入为单位. # 手动添加撤销分隔标志
textPad.pack(expand=YES, fill=BOTH)

scroll = Scrollbar(textPad)
textPad.config(yscrollcommand=scroll.set)
scroll.config(command=textPad.yview)
scroll.pack(side=RIGHT, fill=Y)
textPad.focus_set()  # 给编辑区焦点
root.mainloop()
