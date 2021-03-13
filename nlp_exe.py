# -*- coding: utf-8 -*-
import jieba
import jieba.posseg as pseg
import jieba.analyse
import codecs
import math
import functools
from gensim import corpora
from gensim.models import LdaModel
from gensim import models
from gensim.corpora import Dictionary

string = u'图书评论是近代报刊业兴起后，在世界各国得到长足发展的一种新型评论体裁。而不论是书评理论还是书评实践都有一个不小的疏漏，即忽视了图书的形式因素。'


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


