# -*- coding: utf-8 -*-
# ANSI文件转UTF-8
import codecs
import os

# 文件所在目录
file_path = "D:\\***\\中文文本分类语料（复旦）训练集+测试集（100M）完整版\\train\\C4-Literature"
files = os.listdir(file_path)

for file in files:
    file_name = file_path + '\\' + file
    f = codecs.open(file_name, 'rb', 'ansi')
    ff = f.read()
    file_object = codecs.open(file_path + '\\' + file, 'w', 'utf-8')
    file_object.write(ff)