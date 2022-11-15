#!/usr/bin/python 
# -*- coding:utf-8 -*-
import os
import codecs
import re
import nltk
from nltk.corpus import stopwords
import xlrd
import pandas as pd
# eTOUR、Albergate代码文件读取CAJP（类名、方法名、变量名）
def readcode_2(inputfile, savepath):
    data = pd.read_excel(inputfile)
    #print(data)
    CN = []
    MN = []
    VN = []
    CMT=[]
    code_name=[]
    n=0
    VNfname = savepath + 'CMT.txt'
    ft = codecs.open(VNfname, 'a+', 'utf-8')
    #按行处理
    for num, entity in data.iterrows():
       if '包名' in entity[1]:
           CN.append('换行')
           MN.append('换行')
           VN.append('换行')
           #CMT.append('换行')
           ft.write('\r\n')
           code_name.append(entity[0])
           n=n+1
       elif '类名' in entity[1]:
           CN.append(entity[0])
       elif '域名' in entity[1]:
           VN.append(entity[0])
       elif '方法名' in entity[1]:#方法名
           MN.append(entity[0])
       if '注释' in entity[1]:
           text=str(entity[1])
           #CMT.append(text.split('注释={')[1].replace('\r\n',''))
           #print(entity[1])
           if 'contents: [' in text:
               text=text.split('注释={contents: [')[1]
           else:
               text = text.split('注释={')[1]
           if 'param' in text:
               text.replace('param','')
           if 'author' in text:
               text.replace('author', '')
           if 'return' in text:
                text.replace('return', '')
           if 'version' in text:
               text.replace('version', '')
           if 'throws'in text:
               text.replace('throws', '')
           ft.write(text.replace('\r\n', ''))
           '''else:
               ft.write(text.split('注释={')[1].replace('\r\n',''))'''

           #print(text.split('注释')[1].decode())
    if not os.path.exists(savepath):
        os.makedirs(savepath)
    #存储文件
    #print(CN)
    #print(MN)
    #print(VN)
    #print(n)
    CNname = savepath + 'CN.txt'
    fc = codecs.open(CNname, 'a+', 'utf-8')

    MNfname = savepath + 'MN.txt'
    fm = codecs.open(MNfname, 'a+', 'utf-8')

    VNfname = savepath + 'VN.txt'
    fv = codecs.open(VNfname, 'a+', 'utf-8')

    codefname = savepath + 'Code_TName.txt'
    ff = codecs.open(codefname, 'a+', 'utf-8')
    flag=0
    for cn in CN:
        if '换行' in cn:
            if flag==1:
                fc.write('\r\n')
            else:
                flag=1
        else:
            fc.write(cn+' ')
    flag = 0
    for cn in MN:
        if '换行' in cn:
            if flag == 1:
                fm.write('\r\n')
            else:
                flag = 1
        else:
            fm.write(cn+' ')

    flag = 0
    for cn in VN:
        if '换行' in cn:
            if flag == 1:
                fv.write('\r\n')
            else:
                flag = 1
        else:
            fv.write(cn+' ')

    '''flag = 0
    for cn in CMT:
        if '换行' in cn:
            if flag == 1:
                fv.write('\r\n')
            else:
                flag = 1
        else:
            ft.write(cn+' ')'''

    for i in code_name:
        ff.write(i+'\r\n')

if __name__ == '__main__':
    inputfile='../sample-data/new/SMOS.xlsx'
    savepath='../sample-data/new/'
    readcode_2(inputfile, savepath)
