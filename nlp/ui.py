# -*- coding: utf-8 -*-
from nlp_exe import *
import tkinter as tk
from tkinter import filedialog, dialog
from tkinter import *
import os

tag = 1

file_path = ""
def open_file():
     global  tag
     global file_path
     file_path = filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser('D:/')))
     line ="打开文件成功！"
     # if file_path is not None:
     #       line =  predictkeyword(file_path)
     t.insert("insert", "\n" + line)
     tag = 0

def fenci():
    if tag == 0:
            with open(file=file_path, mode='r+', encoding='utf-8', errors='ignore') as file:
                file_text = file.read()
            line = cut_word(file_text)
            try:t.insert("insert", "\n" + line)
            except:
                print()
            # 参数1：插入方式，参数2：插入的数据
    else:
             var = e.get() #获取输入的信息
             line = cut_word(var)
             t.insert("insert","\n"+line) #参数1：插入方式，参数2：插入的数据


def cixing():
    if tag == 0:
            with open(file=file_path, mode='r+', encoding='utf-8', errors='ignore') as file:
                file_text = file.read()
            line = word_mark(file_text)
            try:t.insert("insert", "\n" + line)
            except:
                    print()# 参数1：插入方式，参数2：插入的数据
    else:
             var = e.get() #获取输入的信息
             line = word_mark(var)
             t.insert("insert","\n"+line) #参数1：插入方式，参数2：插入的数据

def guanjianci():
    if tag == 0:
        with open(file=file_path.replace('text','keyword'), mode='r+', encoding='utf-8',errors='ignore') as file:
            file_text = file.read()
        line = predictkeyword(file_path)
        acc1 = acc(file_path,keyword_path=file_path.replace('text','keyword'))
        rec1 = rec(file_path,keyword_path=file_path.replace('text','keyword'))
        t.insert("insert", "\n关键词：" + file_text)
        t.insert("insert", "\n预测关键词：" + line)

        t.insert("insert", "\n正确率：" + str(acc1))
        t.insert("insert", "\n召回率：" + str(rec1))# 参数1：插入方式，参数2：插入的数据
    else:
        var = e.get()  # 获取输入的信息
        line = key_word_extract(var)
        t.insert("insert", "\n关键词：" + line)  # 参数1：插入方式，参数2：插入的数据

def clean():
    t.delete(0.0, END)


window = tk.Tk()
window.title('NLP_EXE')
window.geometry('550x390')
window.resizable(width=True, height=True)
menubar = tk.Menu(window)
menubar.add_cascade(label='高级设置')
menubar.add_cascade(label='帮助')
window.config(menu=menubar)

l = tk.Label(window, text='欢迎使用本系统！', font=('Arial', 12), width=30, height=1)
# 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高

# 第5步，放置标签
l.pack()  # Label内容content区域放置位置，自动调节尺寸
# 放置lable的方法有：1）l.pack(); 2)l.place();


e = tk.Entry(window, show=None, font=('', 14),width=50)
e.pack()

frm = Frame(window)
frm_L = Frame(frm)
b1 = tk.Button(frm_L, text='打开文件', font=('Arial', 12), width=10, height=1, command=open_file)
b1.pack(side=LEFT)
b2 = tk.Button(frm_L, text='分词', font=('Arial', 12), width=10, height=1, command=fenci)
b2.pack(side=RIGHT)
frm_L.pack(side=LEFT)
frm_R = Frame(frm)
b3 = tk.Button(frm_R, text='词性标注', font=('Arial', 12), width=10, height=1, command=cixing)
b3.pack(side=LEFT)
b4 = tk.Button(frm_R, text='关键词提取', font=('Arial', 12), width=10, height=1,command=guanjianci)
b4.pack(side=RIGHT)
frm_R.pack(side=RIGHT)
frm.pack()
frm1 = Frame(window)
b5 = tk.Button(frm1, text='文本分类', font=('Arial', 12), width=10, height=1)
b5.pack(side=LEFT)
b6 = tk.Button(frm1, text='清屏', font=('Arial', 12), width=10, height=1,command=clean)
b6.pack(side=RIGHT)
frm1.pack()

t = tk.Text(window,height=20)
t.pack()
l1 = tk.Label(window, text='《NLP_EXE_1.0》', font=('Arial', 10), width=30, height=1)
# 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高

# 第5步，放置标签
l1.pack()

window.mainloop()