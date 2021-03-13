# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import filedialog
from tkinter import *
import os
import jieba
import jieba.posseg as pseg
import jieba.analyse
import codecs
import pickle
import docx
from sklearn.naive_bayes import MultinomialNB  # 导入多项式贝叶斯算法

tag = 1

def word_read(filepath):
    file = docx.Document(filepath)
    fulltext = ''
    for i in file.paragraphs:  # 迭代docx文档里面的每一个段落
        fulltext =fulltext+i.text # 保存每一个段落的文本
    return fulltext
# 读取bunch对象
def readbunchobj(path):
    with open(path, "rb") as file_obj:
        bunch = pickle.load(file_obj)
    return bunch

def cut_word(string):  # 精确模式-结巴分词
    seg_list = jieba.cut(string, cut_all=False)
    line = " ".join(seg_list)  # 精确模式
    return line


def cut_stop_word(string):  # 去停用词版本
    stopwords = codecs.open('stopwords.txt', 'r', encoding='utf8').readlines()
    stopwords = [w.strip() for w in stopwords]
    sentence_depart = jieba.cut(string.strip(), cut_all=False)
    line = []
    for word in sentence_depart:
        if word not in stopwords:
            if word != '\t':
                if word != ' ':
                    if word != '\n':
                        if word[0].isdigit() is not True:
                            line.append(word)
    return line


def word_mark(string):  # 词性标注
    sentence = pseg.cut(string)
    line = ""
    for x in sentence:
        line = line + x.word + x.flag + "/"
    return line


def key_word_extract(string):  # 基于tf-idf提取6个关键词
    tags = jieba.analyse.extract_tags(string, topK=6, withWeight=False, allowPOS=())
    line = " ".join(tags)
    return line

def predictkeyword(file_path):
    f = open(file_path, 'r', encoding='utf8', errors='ignore')
    texts = f.read().replace(' ', '')
    texts = texts.replace('\n', '')
    texts = ' '.join(cut_stop_word(texts))
    return key_word_extract(texts)


def Recall_lcs_Gram(str1, str2):
    lstr1 = len(str1)
    lstr2 = len(str2)
    record = [[0 for i in range(lstr2 + 1)] for j in range(lstr1 + 1)]  # 多一位
    maxNum = 0  # 最长匹配长度
    p = 0  # 匹配的起始位
    for i in range(lstr1):
        for j in range(lstr2):
            if str1[i] == str2[j]:
                # 相同则累加
                record[i + 1][j + 1] = record[i][j] + 1
                if record[i + 1][j + 1] > maxNum:
                    # 获取最大匹配长度
                    maxNum = record[i + 1][j + 1]
                    # 记录最大匹配长度的终止位置
                    p = i + 1
    Recall_lcs=maxNum/lstr2
    return Recall_lcs

def Precision_lcs_Gram(str1, str2):
    lstr1 = len(str1)
    lstr2 = len(str2)
    record = [[0 for i in range(lstr2 + 1)] for j in range(lstr1 + 1)]  # 多一位
    maxNum = 0  # 最长匹配长度
    p = 0  # 匹配的起始位
    for i in range(lstr1):
        for j in range(lstr2):
            if str1[i] == str2[j]:
                # 相同则累加
                record[i + 1][j + 1] = record[i][j] + 1
                if record[i + 1][j + 1] > maxNum:
                    # 获取最大匹配长度
                    maxNum = record[i + 1][j + 1]
                    # 记录最大匹配长度的终止位置
                    p = i + 1
    Precision_lcs=maxNum/lstr1
    return Precision_lcs

def acc(file_path,keyword_path):
    f = open(file_path, 'r', encoding='utf8', errors='ignore')
    k = open(keyword_path, 'r', encoding='utf8', errors='ignore')
    texts = f.read()
    key = k.read()
    keys = key.split(' ')
    prekey = key_word_extract(texts).split(' ')
    len_keys = len(keys)
    len_prekey = len(prekey)
    acckey = Precision_lcs_Gram(key.replace(' ', ''),key_word_extract(texts).replace(' ', ''))
    return acckey

def rec(file_path,keyword_path):
    f = open(file_path, 'r', encoding='utf8', errors='ignore')
    k = open(keyword_path, 'r', encoding='utf8', errors='ignore')
    texts = f.read()
    key = k.read()
    keys = key.split(' ')
    prekey = key_word_extract(texts).split(' ')
    len_keys = len(keys)
    len_prekey = len(prekey)
    reckey = Recall_lcs_Gram(key.replace(' ', ''),key_word_extract(texts).replace(' ', ''))
    return reckey


file_path = ""
def open_file():
     global  tag
     global file_path
     file_path = filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser('./')))
     line ="打开文件成功！"
     # if file_path is not None:
     #       line =  predictkeyword(file_path)
     t.insert("insert", "\n" + line)
     #print(file_path)
     tag = 0

def fenci():
    if tag == 0:
        if file_path[-1]=='x':
            file_text = word_read(file_path)
        else:
            with open(file=file_path, mode='rb') as file:
                file_text = file.read()
        line = cut_stop_word(file_text)
        try:t.insert("insert", "\n分词：  " + ' '.join(line))
        except:
            print()
        # 参数1：插入方式，参数2：插入的数据
    else:
             var = e.get() #获取输入的信息
             line = cut_stop_word(var)
             t.insert("insert","\n分词：  "+' '.join(line) )#参数1：插入方式，参数2：插入的数据


def cixing():
    if tag == 0:
        if file_path[-1] == 'x':
            file_text = word_read(file_path)
        else:
            with open(file=file_path, mode='rb') as file:
                file_text = file.read()
        line = word_mark(file_text)
        try:t.insert("insert", "\n词性标注：  " + line)
        except:
                print()# 参数1：插入方式，参数2：插入的数据
    else:
             var = e.get() #获取输入的信息
             line = word_mark(var)
             t.insert("insert","\n词性标注：  "+line) #参数1：插入方式，参数2：插入的数据

def guanjianci():
    global file_path
    if tag == 0:
        file_path =file_path.replace('test_corpus','test_corpus_seg')
        if "train" in file_path:
            file_path = file_path.replace('train_corpus', 'train_corpus_seg')
        with open(file=file_path.replace('text','keyword'), mode='r+', encoding='utf-8',errors='ignore') as file:
            file_text = file.read()
        line = predictkeyword(file_path)
        acc1 = acc(file_path,keyword_path=file_path.replace('text','keyword'))
        rec1 = rec(file_path,keyword_path=file_path.replace('text','keyword'))
        if "seg" in file_path:
            t.insert("insert", "\n预测关键词：\n" + line)
        else:
            t.insert("insert", "\n预测关键词：\n" + line)
            t.insert("insert", "\n正确率：" + str(acc1))
            t.insert("insert", "\n召回率：" + str(rec1))# 参数1：插入方式，参数2：插入的数据
    else:
        var = e.get()  # 获取输入的信息
        line = key_word_extract(var)
        t.insert("insert", "\n关键词：" + line)  # 参数1：插入方式，参数2：插入的数据

def classificate():
    trainpath = "train_word_bag/tfdifspace.dat"
    train_set = readbunchobj(trainpath)
    testpath = "test_word_bag/testspace.dat"
    test_set = readbunchobj(testpath)
    # 训练分类器：输入词袋向量和分类标签，alpha:0.001 alpha越小，迭代次数越多，精度越高
    clf = MultinomialNB(alpha=0.001).fit(train_set.tdm, train_set.label)
    # 预测分类结果
    predicted = clf.predict(test_set.tdm)
    for flabel, file_name, expct_cate in zip(test_set.label, test_set.filenames, predicted):
        list = file_path.split('/')
        len_list = len(list)
        list1 = str(file_name).split('/')
        if list[-2] == list1[-2]:
            if list[-1] == list1[-1]:
                #print(file_name, ": 实际类别:", flabel, " -->预测类别:", expct_cate)
                t.insert("insert","\n"+str(file_name)+": 实际类别:"+str(flabel)+ " -->预测类别:"+str(expct_cate)+"\n")


def clean():
    global tag
    t.delete(0.0, END)
    tag = 1


window = tk.Tk()
window.title('NLP_EXE')
window.geometry('550x390')
window.resizable(width=True, height=True)
menubar = tk.Menu(window)
menubar.add_cascade(label='高级设置')
menubar.add_cascade(label='帮助')
window.config(menu=menubar)

l = tk.Label(window, text='欢迎使用本系统！', font=('Arial', 12,'bold'), width=30, height=1)
# 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高

# 第5步，放置标签
l.pack()  # Label内容content区域放置位置，自动调节尺寸
# 放置lable的方法有：1）l.pack(); 2)l.place();


e = tk.Entry(window, show=None, font=('', 14),width=50)
e.pack()

frm = Frame(window)
frm_L = Frame(frm)
b1 = tk.Button(frm_L, text='打开文件', fg="blue", bg="lightyellow",font=('楷体', 12,'bold'), width=10, height=1, command=open_file)
b1.pack(side=LEFT)
b2 = tk.Button(frm_L, text='分词', fg="blue", bg="lightyellow",font=('楷体', 12,'bold'),width=10, height=1, command=fenci)
b2.pack(side=RIGHT)
frm_L.pack(side=LEFT)
frm_R = Frame(frm)
b3 = tk.Button(frm_R, text='词性标注', fg="blue", bg="lightyellow",font=('楷体', 12,'bold'), width=10, height=1, command=cixing)
b3.pack(side=LEFT)
b4 = tk.Button(frm_R, text='关键词提取', fg="blue", bg="lightyellow",font=('楷体', 12,'bold'), width=10, height=1,command=guanjianci)
b4.pack(side=RIGHT)
frm_R.pack(side=RIGHT)
frm.pack()
frm1 = Frame(window)
# b5 = tk.Button(frm1, text='文本分类', fg="blue", bg="lightyellow",font=('楷体', 12,'bold'),width=10, height=1,command=classificate)
# b5.pack(side=LEFT)
b6 = tk.Button(frm1, text='清屏', fg="blue", bg="lightyellow",font=('楷体', 12,'bold'), width=10, height=1,command=clean)
b6.pack(side=RIGHT)
frm1.pack()

t = tk.Text(window,height=20)
t.pack()
l1 = tk.Label(window, text='《NLP_EXE_1.0》',fg='brown', font=('楷体', 10,'bold'), width=30, height=1)
# 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高

# 第5步，放置标签
l1.pack()


if __name__ == "__main__":
    window.mainloop()