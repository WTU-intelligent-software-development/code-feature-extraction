#!/usr/bin/python 
# -*- coding:utf-8 -*-
import os
import codecs
import re
import nltk
from nltk.corpus import stopwords
import xlrd
import pandas as pd
#正则表达式读取代码的变量名、域名、方法名以及注释
# 正则表达式读取（注释）
def readcode_1(filepath, savepath):
    if not os.path.exists(savepath):
        os.makedirs(savepath)

    fname = savepath + 'CMT.txt'
    fp = codecs.open(fname, 'a+', 'utf-8')

    cfname = savepath + 'CMT_Name.txt'
    fc = codecs.open(cfname, 'a+', 'utf-8')

    #lists = os.listdir(filepath)  # 列出文件夹下所有的目录与文件
    lists = os.walk(filepath)
    for list in lists:
        print (list)
        root = list[0]
        files = list[2]
        for file in files:
            path = os.path.join(root, file)
            #print (path)

    #读取需要的文件
            if os.path.isfile(path):
                f = codecs.open(path, 'rb',encoding='ISO-8859-1')
                lines = f.readlines()
                comment = []
                flag = 0
                index = 0
    #eTPUR提取注释
                ''' for line in lines:
                    #块注释
                    if '/ **' in line:
                        flag=1
                        if re.sub('/ \*\*', '', line).strip()!='':
                            comment.append(re.sub('/ \*\*', '', line).strip())
                    if flag==1 and '*' in line and '/ **' not in line:
                        if re.sub('\*', '', line).strip()!='':
                            comment.append(re.sub('\*', '', line).strip())
                    if '* /' in line:
                        flag=0
                    if '/ / 'in line: # 行注释
                        comment.append(re.sub('/ / ', '', line).strip())'''
                #itrust注释
                for line in lines:
                    #块注释
                    if '/**' in line:
                        flag=1
                        if re.sub('/\*\*', '', line).strip()!='':
                            comment.append(re.sub('/*\\*', '', line).strip())
                    if flag==1 and '*' in line and '/**' not in line:
                        if re.sub('\*', '', line).strip()!='' and '*/'not in line:
                            comment.append(re.sub('\*', '', line).strip())
                        if '*/' in line:
                            if re.sub('\*/', '', line).strip()!='':
                                comment.append(re.sub('\*/', '', line).strip())
                            flag=0
                    if '//'in line:
                        comment.append(re.sub('//', '', line).strip())
                '''for line in lines:
                    if '/*' in line:
                        flag = 1
                        if re.sub('/\*', '', line).strip() != '':
                            comment.append(re.sub('/\*', '', line).strip())
                    if flag == 1 and '*' in line and '/**' not in line:
                        if re.sub('\*', '', line).strip() != '' and '*/' not in line:
                            comment.append(re.sub('\*', '', line).strip())
                        if '*/' in line:
                            if re.sub('\*/', '', line).strip() != '':
                                comment.append(re.sub('\*/', '', line).strip())
                            flag = 0
                    if '//' in line:  # 行注释
                        line=line.split('//')
                        comment.append(re.sub('//', '', line[1]).strip())'''

                print(comment)
                if comment != '':
                    fc.write(file + '\n')
                    for line in comment:
                        fp.write(line+' ')
                    fp.write('\n')



#正则表达式读取变量名、域名、方法名
def readcode_2(filepath, savepath):
    if not os.path.exists(savepath):
        os.makedirs(savepath)
    CN = []
    VN = []
    MN = []

    lists = os.walk(filepath)
    for list in lists:
        print (list)
        root = list[0]
        files = list[2]
        for file in files:
            path = os.path.join(root, file)
            #读取需要的文件
            if os.path.isfile(path):
                f = codecs.open(path, 'rb',encoding='ISO-8859-1')
                lines = f.readlines()
                for line in lines:
                    if 'public' in line or 'private' in line or 'protect' in line or 'void' in line:
                        if 'class' in line:
                            cn=line.split('class')[1]
                            if 'extend' in line:
                                CN.append(cn.split('extend')[1])
                            else:
                                CN.append(cn)
                        else:
                            words = line.split('(')
                            w = words[0].split(' ')
                            word = re.sub('\(', '', w[len(w) - 1])
                            MN.append(word)#方法名

                print(MN)

    CNname = savepath + 'CN.txt'
    fc = codecs.open(CNname, 'a+', 'utf-8')

    MNfname = savepath + 'MN.txt'
    fm = codecs.open(MNfname, 'a+', 'utf-8')

    VNfname = savepath + 'VN.txt'
    fv = codecs.open(VNfname, 'a+', 'utf-8')

    codefname = savepath + 'Code_TName.txt'
    ff = codecs.open(codefname, 'a+', 'utf-8')
    flag = 0
    for cn in CN:
        if '换行' in cn:
            if flag == 1:
                fc.write('\r\n')
            else:
                flag = 1
        else:
            fc.write(cn + ' ')
    flag = 0
    for cn in MN:
        if '换行' in cn:
            if flag == 1:
                fm.write('\r\n')
            else:
                flag = 1
        else:
            fm.write(cn + ' ')

    flag = 0
    for cn in VN:
        if '换行' in cn:
            if flag == 1:
                fv.write('\r\n')
            else:
                flag = 1
        else:
            fv.write(cn + ' ')

    for i in code_name:
        ff.write(i + '\r\n')
    if comment != '':
        fc.write(file + '\n')
        for line in comment:
            fp.write(line + ' ')
        fp.write('\n')


if __name__ == '__main__':

    filepath = '../CoESTData/Albergate/to_be_traced_source_code'
    savepath = '../sample-Data/Albergate_Z/'
    readcode_2(filepath, savepath)


