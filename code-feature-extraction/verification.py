# !/usr/bin/python
#  -*- coding:utf-8 -*-

from __future__ import division
import re
import codecs
import os
import time
import NLP_algorithm


#验证PS039的代码分割实验，比较真集
#eTOUR文件
def eTOUR_verification(select_num,fname):
    truepath = '../sample-data/eTOUR/AnswerSet.txt'
    tname = '../sample-data/eTOUR/UC_FULL_clear.txt'

    #处理真集
    f = codecs.open(truepath, 'rb','utf-8')
    truelines = f.readlines()
    total = 308
    p = 0

    true_class = []
    for trueline in truelines:
        words = trueline.split('\t')
        true_class.append((words[0].lower(), words[1].lower().replace('\r\n', '')))
    #print(len(true_class))

    #文件名
    ucname = '../sample-data/eTOUR/UC_TName.txt'
    ccname =  '../sample-data/eTOUR_all/code_TCName.txt'

    result = NLP_algorithm.vsm_similarity(fname, tname, select_num)
    #result = NLP_algorithm.lsi_similarity(fname, tname, select_num)
    print(result)
    uc=[]
    cc = []
    f = codecs.open(ucname, 'rb','utf-8')
    truelines = f.readlines()
    for trueline in truelines:
        uc.append(trueline.replace('\r\n',''))

    f = codecs.open(ccname, 'rb','utf-8')
    truelines = f.readlines()
    for trueline in truelines:
        cc.append(trueline.replace('\r\n',''))

    result_uToc=[]
    for i in range(len(result)):
        result_uToc.append((uc[result[i][0]-1].lower(),cc[result[i][1]-1].lower()))
    print(result_uToc)
   # print(result_uToc[0][1])
    #print(true_class[0][0])

    #print(true_class[0][1])
    #查找有哪些没找到
    not_find=[]
    #查找有多少个真集数
    for i in range(len(result_uToc)):
        for j in range(len(true_class)):
            if result_uToc[i][0].lower()==true_class[j][0].lower() and result_uToc[i][1].lower()==true_class[j][1].lower():
                p = p + 1
                if result_uToc[i][0].lower()=='uc20.txt' or result_uToc[i][0].lower()=='uc31.txt' or result_uToc[i][0].lower()=='uc32.txt' or result_uToc[i][0].lower()=='uc54.txt':
                    print(result_uToc[i][0],result_uToc[i][1])
                #not_find.append((result_uToc[i][0].split('.'))[0])

    not_find.sort(key=lambda x:int(x[2:]))
    precision = p / len(result)
    recall = p/ total
    f_mearsure = precision * recall * 2 / (precision + recall)
    print(not_find)
    print('Selectivity:%f' % select_num)
    print('precision:%f' % precision)
    print('recall:%f' % recall)
    return select_num, precision, recall,f_mearsure

#iTrust
def iTrust_verification(select_num, fname):
    truepath = '../sample-data/iTrust/answer_req_javacode.txt'
    #fname = '../sample-data/iTrust/MN_CMT_clear.txt'
    tname = '../sample-data/iTrust/UC_clear.txt'

    #处理真集
    f = codecs.open(truepath, 'rb','utf-8')
    truelines = f.readlines()
    total = 418
    p = 0

    true_class = []
    for trueline in truelines:
        words = trueline.split(' ')#'\t'
        true_class.append((words[0].lower(), words[1].lower().replace('\r\n', '')))
    print(len(true_class))

    #文件名
    ucname = '../sample-data/iTrust/UC_TCName.txt'
    ccname =  '../sample-data/iTrust_all/code_TCName.txt'

    #result = NLP_algorithm.vsm_similarity(fname, tname, select_num)
    result = NLP_algorithm.lsi_similarity(fname, tname, select_num)
    print(result)
    uc=[]
    cc = []
    f = codecs.open(ucname, 'rb','utf-8')
    truelines = f.readlines()
    for trueline in truelines:
        uc.append(trueline.replace('\r\n','').split('.')[0])

    f = codecs.open(ccname, 'rb','utf-8')
    truelines = f.readlines()
    for trueline in truelines:
        cc.append(trueline.replace('\n','').split('.')[0])

    result_uToc=[]
    for i in range(len(result)):
        result_uToc.append((uc[result[i][0]-1].lower(),cc[result[i][1]-1].lower()))
    print(result_uToc)
   # print(result_uToc[0][1])
    #print(true_class[0][0])

    #print(true_class[0][1])
    #查找有哪些没找到
    not_find=[]
    #查找有多少个真集数
    for i in range(len(result_uToc)):
        for j in range(len(true_class)):
            if result_uToc[i][0].lower()==true_class[j][0].lower() and result_uToc[i][1].lower()==true_class[j][1].lower():
                p = p + 1
                if result_uToc[i][0].lower()=='uc20.txt' or result_uToc[i][0].lower()=='uc31.txt' or result_uToc[i][0].lower()=='uc32.txt' or result_uToc[i][0].lower()=='uc54.txt':
                    print(result_uToc[i][0],result_uToc[i][1])
                #not_find.append((result_uToc[i][0].split('.'))[0])

    not_find.sort(key=lambda x:int(x[2:]))
    precision = p / len(result)
    recall = p/ total
    f_mearsure = precision * recall * 2 / (precision + recall)
    #print(not_find)
    #print('Selectivity:%f' % select_num)
    #print('precision:%f' % precision)
    #print('recall:%f' % recall)
    return select_num, precision, recall,f_mearsure

def Albergate_verification(select_num,fname):
    truepath = '../sample-data/Albergate/AnswerMatrix.txt'
    tname = '../sample-data/Albergate/re_Full_clear.txt'
    # 处理真集
    f = codecs.open(truepath, 'rb', 'utf-8')
    truelines = f.readlines()
    total = 53
    p = 0
    true_class = []
    for trueline in truelines:
        words = trueline.split(' ')
        true_class.append((words[0].lower(),words[1].replace('\r\n','').lower()))
    #print('true')
    print(len(true_class))
    print(true_class)
    # 文件名
    ucname = '../sample-data/Albergate/re_TCName.txt'
    ccname = '../sample-data/Albergate_all/code_TCName.txt'

    # = NLP_algorithm.vsm_similarity(fname, tname, select_num)
    result = NLP_algorithm.lsi_similarity(fname, tname, select_num)
    uc = []
    cc = []
    f = codecs.open(ucname, 'rb','utf-8')
    truelines = f.readlines()
    for trueline in truelines:
        uc.append(trueline.replace('\r\n', '',))
    f = codecs.open(ccname, 'rb', 'utf-8')
    truelines = f.readlines()
    for trueline in truelines:
        cc.append(trueline.replace('\r\n', '',))

    result_uToc = []
    for i in range(len(result)):
        result_uToc.append((uc[result[i][0] - 1].lower(), cc[result[i][1] - 1].lower()))
    print(result_uToc)
    # 查找有多少个真集数
    for i in range(len(result_uToc)):
        for j in range(len(true_class)):
            if result_uToc[i][0] == true_class[j][0] and result_uToc[i][1] == true_class[j][1]:
                print(result_uToc[i][0], result_uToc[i][1])
                p = p + 1

    precision = p / len(result)
    recall = p / total
    f_mearsure=precision*recall*2/(precision+recall)
    print('Selectivity:%f' % select_num)
    print('precision:%f' % precision)
    print('recall:%f' % recall)
    return select_num, precision, recall,f_mearsure
if __name__ == '__main__':
    result = []
    num = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17,
               0.18, 0.19, 0.2,0.21,0.22,0.23,0.24, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1]
    result = []
    for i in num:
        fname = '../sample-data/XR/itrust_cl.txt'
        select_num, re, pe, f_mearsure = iTrust_verification(i, fname)
        result.append((select_num, pe, re,f_mearsure))

        outpath = '../sample-data/XR/itrust_lsi.txt'  # 取了全部的uc vsm2/只取了uc的第二行
    with open(outpath, 'w')as fp:
        fp.write('selsctivity' + ' ' + 'recall' + ' ' + 'Precision'+ ' ' +'f_mearsure'+ '\n')
        for list in result:
            for i in list:
                fp.write(str(i) + ' ')
            fp.write('\n')
    fp.close()

    '''result = []
    for i in num:
        fname = '../sample-data/Albergate_all/code_clear.txt'
        select_num, re, pe, f_mearsure = Albergate_verification(i, fname)
        result.append((select_num, pe, re, f_mearsure))

        outpath = '../sample-data/Albergate_all/code_all_lsi.txt'  # 取了全部的uc vsm2/只取了uc的第二行
    with open(outpath, 'w')as fp:
        fp.write('selsctivity' + ' ' + 'recall' + ' ' + 'Precision' + ' ' + 'f_mearsure' + '\n')
        for list in result:
            for i in list:
                fp.write(str(i) + ' ')
            fp.write('\n')
    fp.close()'''
    '''for i in num:
        fname = '../sample-data/Albergate/MN_clear.txt'
        select_num, re, pe = Albergate_verification(i,fname)
        result.append((select_num, pe, re))
    outpath = '../sample-data/Albergate_code/MN_lsi.txt'  # 取了全部的uc vsm2/只取了uc的第二行
    with open(outpath, 'w')as fp:
        #fp.write('selsctivity' + ' ' + 'recall' + ' ' + 'Precision' + '\n')
        for list in result:
            for i in list:
                fp.write(str(i) + ' ')
            fp.write('\n')
    fp.close()
    result = []
    for i in num:
        fname = '../sample-data/Albergate/CN_clear.txt'
        select_num, re, pe = Albergate_verification(i,fname)
        result.append((pe, re))

        outpath = '../sample-data/Albergate_code/CN_lsi.txt'  # 取了全部的uc vsm2/只取了uc的第二行
    with open(outpath, 'w')as fp:
        #fp.write('selsctivity' + ' ' + 'recall' + ' ' + 'Precision' + '\n')
        for list in result:
            for i in list:
                fp.write(str(i) + ' ')
            fp.write('\n')
    fp.close()
    result = []
    for i in num:
        fname = '../sample-data/Albergate/VN_clear.txt'
        select_num, re, pe = Albergate_verification(i, fname)
        result.append((pe, re))

    outpath = '../sample-data/Albergate_code/VN_lsi.txt'  # 取了全部的uc vsm2/只取了uc的第二行
    with open(outpath, 'w')as fp:
        #fp.write('selsctivity' + ' ' + 'recall' + ' ' + 'Precision' + '\n')
        for list in result:
            for i in list:
                fp.write(str(i) + ' ')
            fp.write('\n')
    fp.close()
    result = []
    for i in num:
        fname = '../sample-data/Albergate/CMT_clear.txt'
        select_num, re, pe = Albergate_verification(i, fname)
        result.append((pe, re))

    outpath = '../sample-data/Albergate_code/CMT_lsi.txt'  # 取了全部的uc vsm2/只取了uc的第二行
    with open(outpath, 'w')as fp:
        #fp.write('selsctivity' + ' ' + 'recall' + ' ' + 'Precision' + '\n')
        for list in result:
            for i in list:
                fp.write(str(i) + ' ')
            fp.write('\n')
    fp.close()
    result = []
    for i in num:
        fname = '../sample-data/Albergate/CN_MN_clear.txt'
        select_num, re, pe = Albergate_verification(i, fname)
        result.append((pe, re))

    outpath = '../sample-data/Albergate_code/CN_MN_lsi.txt'  # 取了全部的uc vsm2/只取了uc的第二行
    with open(outpath, 'w')as fp:
        #fp.write('selsctivity' + ' ' + 'recall' + ' ' + 'Precision' + '\n')
        for list in result:
            for i in list:
                fp.write(str(i) + ' ')
            fp.write('\n')
    fp.close()
    result = []
    for i in num:
        fname = '../sample-data/Albergate/CN_VN_clear.txt'
        select_num, re, pe = Albergate_verification(i, fname)
        result.append((pe, re))

    outpath = '../sample-data/Albergate_code/CN_VN_lsi.txt'  # 取了全部的uc vsm2/只取了uc的第二行
    with open(outpath, 'w')as fp:
        #fp.write('selsctivity' + ' ' + 'recall' + ' ' + 'Precision' + '\n')
        for list in result:
            for i in list:
                fp.write(str(i) + ' ')
            fp.write('\n')
    fp.close()
    result = []
    for i in num:
        fname = '../sample-data/Albergate/CN_CMT_clear.txt'
        select_num, re, pe = Albergate_verification(i, fname)
        result.append((pe, re))

    outpath = '../sample-data/Albergate_code/CN_CMT_lsi.txt'  # 取了全部的uc vsm2/只取了uc的第二行
    with open(outpath, 'w')as fp:
        #fp.write('selsctivity' + ' ' + 'recall' + ' ' + 'Precision' + '\n')
        for list in result:
            for i in list:
                fp.write(str(i) + ' ')
            fp.write('\n')
    fp.close()
    result = []
    for i in num:
        fname = '../sample-data/Albergate/MN_CMT_clear.txt'
        select_num, re, pe = Albergate_verification(i, fname)
        result.append((pe, re))
    outpath = '../sample-data/Albergate_code/MN_CMT_lsi.txt'
    with open(outpath, 'w')as fp:
        #fp.write('selsctivity' + ' ' + 'recall' + ' ' + 'Precision' + '\n')
        for list in result:
            for i in list:
                fp.write(str(i) + ' ')
            fp.write('\n')
    fp.close()
    result = []
    for i in num:
        fname = '../sample-data/Albergate/VN_CMT_clear.txt'
        select_num, re, pe = Albergate_verification(i, fname)
        result.append((pe, re))

    outpath = '../sample-data/Albergate_code/VN_CMT_lsi.txt'  # 取了全部的uc vsm2/只取了uc的第二行
    with open(outpath, 'w')as fp:
        #fp.write('selsctivity' + ' ' + 'recall' + ' ' + 'Precision' + '\n')
        for list in result:
            for i in list:
                fp.write(str(i) + ' ')
            fp.write('\n')
    fp.close()
    result = []
    for i in num:
        fname = '../sample-data/Albergate/CN_MN_CMT_clear.txt'
        select_num, re, pe = Albergate_verification(i, fname)
        result.append((pe, re))

    outpath = '../sample-data/Albergate_code/CN_MN_CMT_lsi.txt'  # 取了全部的uc vsm2/只取了uc的第二行
    with open(outpath, 'w')as fp:
        #fp.write('selsctivity' + ' ' + 'recall' + ' ' + 'Precision' + '\n')
        for list in result:
            for i in list:
                fp.write(str(i) + ' ')
            fp.write('\n')
    fp.close()
    result = []
    for i in num:
        fname = '../sample-data/Albergate/CN_VN_CMT_clear.txt'
        select_num, re, pe = Albergate_verification(i, fname)
        result.append((pe, re))

    outpath = '../sample-data/Albergate_code/CN_VN_CMT_lsi.txt'  # 取了全部的uc vsm2/只取了uc的第二行
    with open(outpath, 'w')as fp:
        #fp.write('selsctivity' + ' ' + 'recall' + ' ' + 'Precision' + '\n')
        for list in result:
            for i in list:
                fp.write(str(i) + ' ')
            fp.write('\n')
    fp.close()
    result = []
    for i in num:
        fname = '../sample-data/Albergate/MN_VN_CMT_clear.txt'
        select_num, re, pe = Albergate_verification(i, fname)
        result.append((pe, re))

    outpath = '../sample-data/Albergate_code/MN_VN_CMT_lsi.txt'  # 取了全部的uc vsm2/只取了uc的第二行
    with open(outpath, 'w')as fp:
        #fp.write('selsctivity' + ' ' + 'recall' + ' ' + 'Precision' + '\n')
        for list in result:
            for i in list:
                fp.write(str(i) + ' ')
            fp.write('\n')
    fp.close()

    result = []
    for i in num:
        fname = '../sample-data/Albergate/CN_MN_VN_CMT_clear.txt'
        select_num, re, pe = Albergate_verification(i, fname)
        result.append((pe, re))

        outpath = '../sample-data/Albergate_code/CN_MN_VN_CMT_lsi.txt'  # 取了全部的uc vsm2/只取了uc的第二行
    with open(outpath, 'w')as fp:
        #fp.write('selsctivity' + ' ' + 'recall' + ' ' + 'Precision' + '\n')
        for list in result:
            for i in list:
                fp.write(str(i) + ' ')
            fp.write('\n')
    fp.close()
    for i in num:
        fname = '../sample-data/iTrust/MN_clear.txt'
        select_num, re, pe = eTOUR_UCtoCCverification(i,fname)
        result.append((select_num, pe, re))
    outpath = '../sample-data/iTrust_code/MN_lsi.txt'  # 取了全部的uc vsm2/只取了uc的第二行
    with open(outpath, 'w')as fp:
        fp.write('selsctivity' + ' ' + 'recall' + ' ' + 'Precision' + '\n')
        for list in result:
            for i in list:
                fp.write(str(i) + ' ')
            fp.write('\n')
    fp.close()
    result = []
    for i in num:
        fname = '../sample-data/iTrust/CN_clear.txt'
        select_num, re, pe = eTOUR_UCtoCCverification(i, fname)
        result.append((select_num, pe, re))

        outpath = '../sample-data/iTrust_code/CN_lsi.txt'  # 取了全部的uc vsm2/只取了uc的第二行
    with open(outpath, 'w')as fp:
        fp.write('selsctivity' + ' ' + 'recall' + ' ' + 'Precision' + '\n')
        for list in result:
            for i in list:
                fp.write(str(i) + ' ')
            fp.write('\n')
    fp.close()
    result = []
    for i in num:
        fname = '../sample-data/iTrust/VN_clear.txt'
        select_num, re, pe = eTOUR_UCtoCCverification(i, fname)
        result.append((select_num, pe, re))

    outpath = '../sample-data/iTrust_code/VN_lsi.txt'  # 取了全部的uc vsm2/只取了uc的第二行
    with open(outpath, 'w')as fp:
        fp.write('selsctivity' + ' ' + 'recall' + ' ' + 'Precision' + '\n')
        for list in result:
            for i in list:
                fp.write(str(i) + ' ')
            fp.write('\n')
    fp.close()
    result = []
    for i in num:
        fname = '../sample-data/iTrust/CMT_clear.txt'
        select_num, re, pe = eTOUR_UCtoCCverification(i, fname)
        result.append((select_num, pe, re))

    outpath = '../sample-data/iTrust_code/CMT_lsi.txt'  # 取了全部的uc vsm2/只取了uc的第二行
    with open(outpath, 'w')as fp:
        fp.write('selsctivity' + ' ' + 'recall' + ' ' + 'Precision' + '\n')
        for list in result:
            for i in list:
                fp.write(str(i) + ' ')
            fp.write('\n')
    fp.close()
    result = []
    for i in num:
        fname = '../sample-data/iTrust/CN_MN_clear.txt'
        select_num, re, pe = eTOUR_UCtoCCverification(i, fname)
        result.append((select_num, pe, re))

    outpath = '../sample-data/iTrust_code/CN_MN_lsi.txt'  # 取了全部的uc vsm2/只取了uc的第二行
    with open(outpath, 'w')as fp:
        fp.write('selsctivity' + ' ' + 'recall' + ' ' + 'Precision' + '\n')
        for list in result:
            for i in list:
                fp.write(str(i) + ' ')
            fp.write('\n')
    fp.close()
    result = []
    for i in num:
        fname = '../sample-data/iTrust/CN_VN_clear.txt'
        select_num, re, pe = eTOUR_UCtoCCverification(i, fname)
        result.append((select_num, pe, re))

    outpath = '../sample-data/iTrust_code/CN_VN_lsi.txt'  # 取了全部的uc vsm2/只取了uc的第二行
    with open(outpath, 'w')as fp:
        fp.write('selsctivity' + ' ' + 'recall' + ' ' + 'Precision' + '\n')
        for list in result:
            for i in list:
                fp.write(str(i) + ' ')
            fp.write('\n')
    fp.close()
    result = []
    for i in num:
        fname = '../sample-data/iTrust/CN_CMT_clear.txt'
        select_num, re, pe = eTOUR_UCtoCCverification(i, fname)
        result.append((select_num, pe, re))

    outpath = '../sample-data/iTrust_code/CN_CMT_lsi.txt'  # 取了全部的uc vsm2/只取了uc的第二行
    with open(outpath, 'w')as fp:
        fp.write('selsctivity' + ' ' + 'recall' + ' ' + 'Precision' + '\n')
        for list in result:
            for i in list:
                fp.write(str(i) + ' ')
            fp.write('\n')
    fp.close()
    result = []
    for i in num:
        fname = '../sample-data/iTrust/MN_CMT_clear.txt'
        select_num, re, pe = eTOUR_UCtoCCverification(i, fname)
        result.append((select_num, pe, re))
    outpath =  '../sample-data/iTrust_code/MN_CMT_lsi.txt'
    with open(outpath, 'w')as fp:
        fp.write('selsctivity' + ' ' + 'recall' + ' ' + 'Precision' + '\n')
        for list in result:
            for i in list:
                fp.write(str(i) + ' ')
            fp.write('\n')
    fp.close()
    result = []
    for i in num:
        fname = '../sample-data/iTrust/VN_CMT_clear.txt'
        select_num, re, pe = eTOUR_UCtoCCverification(i, fname)
        result.append((select_num, pe, re))

    outpath = '../sample-data/iTrust_code/VN_CMT_lsi.txt'  # 取了全部的uc vsm2/只取了uc的第二行
    with open(outpath, 'w')as fp:
        fp.write('selsctivity' + ' ' + 'recall' + ' ' + 'Precision' + '\n')
        for list in result:
            for i in list:
                fp.write(str(i) + ' ')
            fp.write('\n')
    fp.close()
    result = []
    for i in num:
        fname = '../sample-data/iTrust/CN_MN_CMT_clear.txt'
        select_num, re, pe = eTOUR_UCtoCCverification(i, fname)
        result.append((select_num, pe, re))

    outpath = '../sample-data/iTrust_code/CN_MN_CMT_lsi.txt'  # 取了全部的uc vsm2/只取了uc的第二行
    with open(outpath, 'w')as fp:
        fp.write('selsctivity' + ' ' + 'recall' + ' ' + 'Precision' + '\n')
        for list in result:
            for i in list:
                fp.write(str(i) + ' ')
            fp.write('\n')
    fp.close()
    result = []
    for i in num:
        fname = '../sample-data/iTrust/CN_VN_CMT_clear.txt'
        select_num, re, pe = eTOUR_UCtoCCverification(i, fname)
        result.append((select_num, pe, re))

    outpath = '../sample-data/iTrust_code/CN_VN_CMT_lsi.txt'  # 取了全部的uc vsm2/只取了uc的第二行
    with open(outpath, 'w')as fp:
        fp.write('selsctivity' + ' ' + 'recall' + ' ' + 'Precision' + '\n')
        for list in result:
            for i in list:
                fp.write(str(i) + ' ')
            fp.write('\n')
    fp.close()
    result = []
    for i in num:
        fname = '../sample-data/iTrust/MN_VN_CMT_clear.txt'
        select_num, re, pe = eTOUR_UCtoCCverification(i, fname)
        result.append((select_num, pe, re))

    outpath = '../sample-data/iTrust_code/MN_VN_CMT_lsi.txt'  # 取了全部的uc vsm2/只取了uc的第二行
    with open(outpath, 'w')as fp:
        fp.write('selsctivity' + ' ' + 'recall' + ' ' + 'Precision' + '\n')
        for list in result:
            for i in list:
                fp.write(str(i) + ' ')
            fp.write('\n')
    fp.close()

    result = []
    for i in num:
        fname = '../sample-data/iTrust/CN_MN_VN_CMT_clear.txt'
        select_num, re, pe = eTOUR_UCtoCCverification(i, fname)
        result.append((select_num, pe, re))

        outpath = '../sample-data/iTrust_code/CN_MN_VN_CMT_lsi.txt'  # 取了全部的uc vsm2/只取了uc的第二行
    with open(outpath, 'w')as fp:
        fp.write('selsctivity' + ' ' + 'recall' + ' ' + 'Precision' + '\n')
        for list in result:
            for i in list:
                fp.write(str(i) + ' ')
            fp.write('\n')
    fp.close()'''

    '''result = []
    for i in num:
        fname = '../sample-data/iTrust/MN_VN_clear.txt'
        select_num, re, pe = eTOUR_UCtoCCverification(i, fname)
        result.append((select_num, pe, re))

        outpath = '../sample-data/iTrust_code/MN_VN_vsm.txt'  # 取了全部的uc vsm2/只取了uc的第二行
    with open(outpath, 'w')as fp:
        fp.write('selsctivity' + ' ' + 'recall' + ' ' + 'Precision' + '\n')
        for list in result:
            for i in list:
                fp.write(str(i) + ' ')
            fp.write('\n')
    fp.close()'''
    '''for i in num:
        fname = '../sample-data/eTOUR/MN_clear.txt'
        select_num, re, pe = eTOUR_UCtoCCverification(i, fname)
        result.append((select_num, pe, re))
    outpath = '../sample-data/eTOUR_code/MN_lsi.txt'  # 取了全部的uc vsm2/只取了uc的第二行
    with open(outpath, 'w')as fp:
        fp.write('selsctivity' + ' ' + 'recall' + ' ' + 'Precision' + '\n')
        for list in result:
            for i in list:
                fp.write(str(i) + ' ')
            fp.write('\n')
    fp.close()
    result = []
    for i in num:
        fname = '../sample-data/eTOUR/CN_clear.txt'
        select_num, re, pe = eTOUR_UCtoCCverification(i, fname)
        result.append((select_num, pe, re))

        outpath = '../sample-data/eTOUR_code/CN_lsi.txt'  # 取了全部的uc vsm2/只取了uc的第二行
    with open(outpath, 'w')as fp:
        fp.write('selsctivity' + ' ' + 'recall' + ' ' + 'Precision' + '\n')
        for list in result:
            for i in list:
                fp.write(str(i) + ' ')
            fp.write('\n')
    fp.close()
    result = []
    for i in num:
        fname = '../sample-data/eTOUR/VN_clear.txt'
        select_num, re, pe = eTOUR_UCtoCCverification(i, fname)
        result.append((select_num, pe, re))

    outpath = '../sample-data/eTOUR_code/VN_lsi.txt'  # 取了全部的uc vsm2/只取了uc的第二行
    with open(outpath, 'w')as fp:
        fp.write('selsctivity' + ' ' + 'recall' + ' ' + 'Precision' + '\n')
        for list in result:
            for i in list:
                fp.write(str(i) + ' ')
            fp.write('\n')
    fp.close()
    result = []
    for i in num:
        fname = '../sample-data/eTOUR/CMT_clear.txt'
        select_num, re, pe = eTOUR_UCtoCCverification(i, fname)
        result.append((select_num, pe, re))

    outpath = '../sample-data/eTOUR_code/CMT_lsi.txt'  # 取了全部的uc vsm2/只取了uc的第二行
    with open(outpath, 'w')as fp:
        fp.write('selsctivity' + ' ' + 'recall' + ' ' + 'Precision' + '\n')
        for list in result:
            for i in list:
                fp.write(str(i) + ' ')
            fp.write('\n')
    fp.close()
    result = []
    for i in num:
        fname = '../sample-data/eTOUR/CN_MN_clear.txt'
        select_num, re, pe = eTOUR_UCtoCCverification(i, fname)
        result.append((select_num, pe, re))

    outpath = '../sample-data/eTOUR_code/CN_MN_lsi.txt'  # 取了全部的uc vsm2/只取了uc的第二行
    with open(outpath, 'w')as fp:
        fp.write('selsctivity' + ' ' + 'recall' + ' ' + 'Precision' + '\n')
        for list in result:
            for i in list:
                fp.write(str(i) + ' ')
            fp.write('\n')
    fp.close()
    result = []
    for i in num:
        fname = '../sample-data/eTOUR/CN_VN_clear.txt'
        select_num, re, pe = eTOUR_UCtoCCverification(i, fname)
        result.append((select_num, pe, re))

    outpath = '../sample-data/eTOUR_code/CN_VN_lsi.txt'  # 取了全部的uc vsm2/只取了uc的第二行
    with open(outpath, 'w')as fp:
        fp.write('selsctivity' + ' ' + 'recall' + ' ' + 'Precision' + '\n')
        for list in result:
            for i in list:
                fp.write(str(i) + ' ')
            fp.write('\n')
    fp.close()
    result = []
    for i in num:
        fname = '../sample-data/eTOUR/CN_CMT_clear.txt'
        select_num, re, pe = eTOUR_UCtoCCverification(i, fname)
        result.append((select_num, pe, re))

    outpath = '../sample-data/eTOUR_code/CN_CMT_lsi.txt'  # 取了全部的uc vsm2/只取了uc的第二行
    with open(outpath, 'w')as fp:
        fp.write('selsctivity' + ' ' + 'recall' + ' ' + 'Precision' + '\n')
        for list in result:
            for i in list:
                fp.write(str(i) + ' ')
            fp.write('\n')
    fp.close()
    result = []
    for i in num:
        fname = '../sample-data/eTOUR/MN_CMT_clear.txt'
        select_num, re, pe = eTOUR_UCtoCCverification(i, fname)
        result.append((select_num, pe, re))
    outpath = '../sample-data/eTOUR_code/MN_CMT_lsi.txt'
    with open(outpath, 'w')as fp:
        fp.write('selsctivity' + ' ' + 'recall' + ' ' + 'Precision' + '\n')
        for list in result:
            for i in list:
                fp.write(str(i) + ' ')
            fp.write('\n')
    fp.close()
    result = []
    for i in num:
        fname = '../sample-data/eTOUR/MN_VN_clear.txt'
        select_num, re, pe = eTOUR_UCtoCCverification(i, fname)
        result.append((select_num, pe, re))
    outpath = '../sample-data/eTOUR_code/MN_VN_lsi.txt'
    with open(outpath, 'w')as fp:
        fp.write('selsctivity' + ' ' + 'recall' + ' ' + 'Precision' + '\n')
        for list in result:
            for i in list:
                fp.write(str(i) + ' ')
            fp.write('\n')
    fp.close()
    result = []
    for i in num:
        fname = '../sample-data/eTOUR/VN_CMT_clear.txt'
        select_num, re, pe = eTOUR_UCtoCCverification(i, fname)
        result.append((select_num, pe, re))

    outpath = '../sample-data/eTOUR_code/VN_CMT_lsi.txt'  # 取了全部的uc vsm2/只取了uc的第二行
    with open(outpath, 'w')as fp:
        fp.write('selsctivity' + ' ' + 'recall' + ' ' + 'Precision' + '\n')
        for list in result:
            for i in list:
                fp.write(str(i) + ' ')
            fp.write('\n')
    fp.close()
    result = []
    for i in num:
        fname = '../sample-data/eTOUR/CN_MN_CMT_clear.txt'
        select_num, re, pe = eTOUR_UCtoCCverification(i, fname)
        result.append((select_num, pe, re))

    outpath = '../sample-data/iTrust_code/CN_MN_CMT_lsi.txt'  # 取了全部的uc vsm2/只取了uc的第二行
    with open(outpath, 'w')as fp:
        fp.write('selsctivity' + ' ' + 'recall' + ' ' + 'Precision' + '\n')
        for list in result:
            for i in list:
                fp.write(str(i) + ' ')
            fp.write('\n')
    fp.close()
    result = []
    for i in num:
        fname = '../sample-data/eTOUR/CN_VN_CMT_clear.txt'
        select_num, re, pe = eTOUR_UCtoCCverification(i, fname)
        result.append((select_num, pe, re))

    outpath = '../sample-data/eTOUR_code/CN_VN_CMT_lsi.txt'  # 取了全部的uc vsm2/只取了uc的第二行
    with open(outpath, 'w')as fp:
        fp.write('selsctivity' + ' ' + 'recall' + ' ' + 'Precision' + '\n')
        for list in result:
            for i in list:
                fp.write(str(i) + ' ')
            fp.write('\n')
    fp.close()

    result = []
    for i in num:
        fname = '../sample-data/eTOUR/CN_MN_VN_clear.txt'
        select_num, re, pe = eTOUR_UCtoCCverification(i, fname)
        result.append((select_num, pe, re))

    outpath = '../sample-data/eTOUR_code/CN_MN_VN_lsi.txt'  # 取了全部的uc vsm2/只取了uc的第二行
    with open(outpath, 'w')as fp:
        fp.write('selsctivity' + ' ' + 'recall' + ' ' + 'Precision' + '\n')
        for list in result:
            for i in list:
                fp.write(str(i) + ' ')
            fp.write('\n')
    fp.close()
    result = []
    for i in num:
        fname = '../sample-data/eTOUR/MN_VN_CMT_clear.txt'
        select_num, re, pe = eTOUR_UCtoCCverification(i, fname)
        result.append((select_num, pe, re))

    outpath = '../sample-data/eTOUR_code/MN_VN_CMT_lsi.txt'  # 取了全部的uc vsm2/只取了uc的第二行
    with open(outpath, 'w')as fp:
        fp.write('selsctivity' + ' ' + 'recall' + ' ' + 'Precision' + '\n')
        for list in result:
            for i in list:
                fp.write(str(i) + ' ')
            fp.write('\n')
    fp.close()

    result = []
    for i in num:
        fname = '../sample-data/eTOUR/CN_MN_VN_CMT_clear.txt'
        select_num, re, pe = eTOUR_UCtoCCverification(i, fname)
        result.append((select_num, pe, re))

        outpath = '../sample-data/eTOUR_code/CN_MN_VN_CMT_lsi.txt'  # 取了全部的uc vsm2/只取了uc的第二行
    with open(outpath, 'w')as fp:
        fp.write('selsctivity' + ' ' + 'recall' + ' ' + 'Precision' + '\n')
        for list in result:
            for i in list:
                fp.write(str(i) + ' ')
            fp.write('\n')
    fp.close()'''






