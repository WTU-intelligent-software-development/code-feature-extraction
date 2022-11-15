import re
import os
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import codecs
#打开并读取文件
def Data_clear(path,output_path):
    if os.path.isfile(path):
        f = codecs.open(path, 'rb', 'utf-8')
        lines = f.readlines()
        filtered = []
    for text_list in lines:
        # 1，分词
        text_list = nltk.word_tokenize(text_list)
        # 2，去除标点符号和停用词
        english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%','<','>','/','@','»','¿','b','p','©','=','\\','//','ï','¿/']
        text_list = [word for word in text_list if word not in english_punctuations]
        stops = set(stopwords.words("english"))
        text_list = [word for word in text_list if word not in stops]
        # 3，词性标注并保留动词和名词
        text_list = nltk.pos_tag(text_list)
        text_list = [name for name,value in text_list if value in ['NN','NNP','NNPS','NNS','VB','VBD','VBG','VBN','VBP','VBZ']]
        filtered=filtered+text_list
        filtered.append('\n')
        #print(filtered)
        #print(type(filtered))
        # 4，词干提取并写入文件
    with open(output_path, 'w',encoding='utf-8')as fp:
        for i in filtered:
            porter_stemmer = PorterStemmer()
            if '\n' in i:
                fp.write(porter_stemmer.stem(i))
            else:
                fp.write(porter_stemmer.stem(i)+' ')
                #print(i)
    fp.close()


#处理itrust断行的问题
def iTrust_clear(path,):
    if os.path.isfile(path):
        f = codecs.open(path, 'rb', 'utf-8')
        lines = f.readlines()


if __name__ == '__main__':
    #path = '../sample-Data/iTrust_all/code_Full.txt'
    #output_path = '../sample-Data/iTrust_all/code_clear.txt'
    #Data_clear(path, output_path)
    '''path = '../sample-Data/XR/etour.txt'
    output_path = '../sample-Data/XR/etour_cl.txt'
    Data_clear(path, output_path)'''
    '''path = '../sample-Data/XR/itrust.txt'
    output_path = '../sample-Data/XR/itrust_cl.txt'
    Data_clear(path, output_path)
    path = '../sample-Data/XR/SMOS.txt'
    output_path = '../sample-Data/XR/SMOS_cl.txt'
    Data_clear(path, output_path)'''
    '''path = '../sample-Data/XR/albergate.txt'
    output_path = '../sample-Data/XR/albergate_cl.txt'
    Data_clear(path, output_path)'''
    path = '../sample-Data/XR/easyclinic.txt'
    output_path = '../sample-Data/XR/easyclinic_cl.txt'
    Data_clear(path, output_path)

    '''path = '../sample-Data/eTOUR/CN_CMT.txt'
    output_path = '../sample-Data/eTOUR/CN_CMT_clear.txt'
    Data_clear(path, output_path)'''
    '''path = '../sample-Data/iTrust/VN.txt'
    output_path = '../sample-Data/iTrust/VN_clear.txt'
    Data_clear(path, output_path)

    path = '../sample-Data/eTOUR/CN.txt'
    output_path = '../sample-Data/iTrust/CN_clear.txt'
    Data_clear(path, output_path)

    path = '../sample-Data/iTrust/MN.txt'
    output_path = '../sample-Data/iTrust/MN_clear.txt'
    Data_clear(path, output_path)
    
    path = '../sample-Data/Albergate/CMT.txt'
    output_path = '../sample-Data/Albergate/CMT_clear.txt'
    Data_clear(path, output_path)'''

    '''path='../sample-Data/Albergate/CN_CMT.txt'
    output_path = '../sample-Data/Albergate/CN_CMT_clear.txt'
    Data_clear(path,output_path)

    path ='../sample-Data/Albergate/CN_MN.txt'
    output_path = '../sample-Data/Albergate/CN_MN_clear.txt'
    Data_clear(path,output_path)

    path ='../sample-Data/Albergate/CN_VN.txt'
    output_path = '../sample-Data/Albergate/CN_VN_clear.txt'
    Data_clear(path,output_path)

    path ='../sample-Data/Albergate/MN_VN.txt'
    output_path = '../sample-Data/Albergate/MN_VN_clear.txt'
    Data_clear(path,output_path)

    path ='../sample-Data/Albergate/MN_CMT.txt'
    output_path = '../sample-Data/Albergate/MN_CMT_clear.txt'
    Data_clear(path,output_path)

    path='../sample-Data/Albergate/VN_CMT.txt'
    output_path = '../sample-Data/Albergate/VN_CMT_clear.txt'
    Data_clear(path,output_path)

    path='../sample-Data/Albergate/CN_MN_VN.txt'
    output_path = '../sample-Data/Albergate/CN_MN_VN_clear.txt'
    Data_clear(path,output_path)

    path ='../sample-Data/Albergate/CN_VN_CMT.txt'
    output_path = '../sample-Data/Albergate/CN_VN_CMT_clear.txt'
    Data_clear(path, output_path)

    path ='../sample-Data/Albergate/CN_MN_CMT.txt'
    output_path = '../sample-Data/Albergate/CN_MN_CMT_clear.txt'
    Data_clear(path, output_path)

    path ='../sample-Data/Albergate/MN_VN_CMT.txt'
    output_path = '../sample-Data/Albergate/MN_VN_CMT_clear.txt'
    Data_clear(path, output_path)

    path ='../sample-Data/Albergate/CN_MN_VN_CMT.txt'
    output_path = '../sample-Data/Albergate/CN_MN_VN_CMT_clear.txt'
    Data_clear(path, output_path)'''
    path ='../sample-Data/EasyClinic/CMT.txt'
    output_path = '../sample-Data/EasyClinic/CMT_clear.txt'
    Data_clear(path, output_path)

