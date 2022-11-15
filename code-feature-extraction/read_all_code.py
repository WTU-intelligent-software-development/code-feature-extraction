#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import codecs
import re
import nltk
from nltk.corpus import stopwords
import xlrd
import pandas as pd
#读取code里面的全部内容
def read_Albergate_code_full(filepath,savepath):
    if not os.path.exists(savepath):
        os.makedirs(savepath)

    fname = savepath + 'albergate.txt'
    fp = codecs.open(fname, 'a+', 'utf-8')
#存储表名
    cfname = savepath + 'albergate_TCName.txt'
    fc = codecs.open(cfname, 'a+', 'utf-8')

    lists = os.listdir(filepath)  # 按顺序列出文件夹下所有的目录与文件
    flag = 0
    comment = []
    for list in lists:
        if 'java' in list:
            fc.write(list + '\r\n')  # 将文件名保存至TCName文本文件中
            path = os.path.join(filepath, list)
            print (list)#输出每个文件的地址
            if os.path.isfile(path):#如果该地址存在，读取文档中的内容
                f = codecs.open(path, 'rb',encoding='ISO-8859-1')
                lines = f.readlines()
                flag_1=0
                flag = 0
                # 将需求或软件制品文本保存至文本文件
                for line in lines:
                    index=0
                    # eTPUR提取注释
                    '''if '/ **' in line:
                        flag = 1
                        index=1
                        if re.sub('/ \*\*', '', line).strip() != '':
                            comment.append(re.sub('/ \*\*', '', line).strip())
                    if flag == 1 and '*' in line and '/ **' not in line:
                        index = 1
                        if re.sub('\*', '', line).strip() != '':
                            comment.append(re.sub('\*', '', line).strip())
                    if '* /' in line:
                        index = 1
                        flag = 0
                    if '/ / ' in line:  # 行注释
                        index = 1
                        comment.append(re.sub('/ / ', '', line).strip())'''
                    # itrust注释
                    # 块注释
                    '''if '/*' in line and '/**' not in line:
                        flag = 1
                        index = 1
                        if re.sub('/*', '', line).strip() != '':
                            comment.append(re.sub('/*', '', line).strip())
                    if flag == 1 and '*' in line and '/*' not in line:
                        index = 1
                        if re.sub('\*', '', line).strip() != '' and '*/' not in line:
                            comment.append(re.sub('\*', '', line).strip())
                        if '*/' in line:
                            flag = 0
                            if re.sub('\*/', '', line).strip() != '':
                                comment.append(re.sub('\*/', '', line).strip())
                    if '/**' in line:
                        index = 1
                        flag_1 = 1
                        if re.sub('/\*\*', '', line).strip() != '':
                            comment.append(re.sub('/*\\*', '', line).strip())
                    if flag_1 == 1 and '*' in line and '/**' not in line:
                        index = 1
                        if re.sub('\*', '', line).strip() != '' and '*/' not in line:
                            comment.append(re.sub('\*', '', line).strip())
                        if '*/' in line:
                            flag_1 = 0
                            if re.sub('\*/', '', line).strip() != '':
                                comment.append(re.sub('\*/', '', line).strip())

                    if '//' in line:
                        index = 1
                        comment.append(re.sub('//', '', line).strip())'''
                    #albergate
                    if '/*' in line:
                        index = 1
                        flag = 1
                        if re.sub('/\*', '', line).strip() != '':
                            comment.append(re.sub('/\*', '', line).strip())
                    if flag == 1 and '*' in line and '/**' not in line:
                        index = 1
                        if re.sub('\*', '', line).strip() != '' and '*/' not in line:
                            comment.append(re.sub('\*', '', line).strip())
                        if '*/' in line:
                            if re.sub('\*/', '', line).strip() != '':
                                comment.append(re.sub('\*/', '', line).strip())
                            flag = 0
                        if '//' in line:  # 行注释
                            index = 1
                            line = line.split('//')
                            comment.append(re.sub('//', '', line[1]).strip())
                    if index!=1:
                        line=line.strip('\r\n')
                        line=line.strip('\n')
                        fp.write(line+' ')
                fp.write('\r\n')

if __name__ == '__main__':
    '''filepath = '../CoESTData/eTOUR/CC/'
    savepath = '../sample-Data/XR/'''''
    '''filepath = '../CoESTData/iTrust/iTrust-code/'
    savepath = '../sample-Data/XR/'''''
    '''filepath = '../CoESTData/SMOS/cc(English)/'
    savepath = '../sample-Data/XR/'''''
    filepath = '../CoESTData/Albergate/to_be_traced_source_code/'
    savepath = '../sample-Data/XR/'
    read_Albergate_code_full(filepath, savepath)