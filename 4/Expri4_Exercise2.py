# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Expri4_Exercise2
   Description :
   Author :       Adminstrator
   date：          2019/5/13
-------------------------------------------------
   Change Activity:
                   2019/5/13:
-------------------------------------------------
"""
'''
For a text file.
(a) Find the 20 most common words前20个常见单词
(b) How many unique words are used?只出现一次的单词
(c) How many words are used at least 5 times?出现至少5次的单词
(d) Write the 40 most common words, and their counts, to a file 将前40常见的单词写到新的文件
'''

def countfile(filename):
    import os
    import re
    import string

    path = os.getcwd() +'/'+filename
    content = []
    dic={}

    fp = open(path, 'r')

    content = fp.readlines()

    fp.close

    for line in content:
        line=line.strip('\n')
        line = line.strip(string.digits)
        line = line.strip(string.punctuation)
        line = line.rstrip(string.punctuation)

        for i in line.split(' '):
            if i in dic:
                dic[i]+=1
            else:
                tempdic={i:1}
                dic.update(tempdic)
    del dic['-'] #删除无法切取的单词，根据不同的txt文本预测试判断
    list= sorted(dic.items(),key=lambda x:x[1],reverse=True)

    for i in range(20):
        print(list[i])

    count=0
    for i in list:
        if i[1]==1:
            count+=1

    print('有',count,'个只出现过一次的单词')

    count=0
    for i in list:
        if i[1]>=5:
            count+=1
    print('有',count,'个至少出现过5次的单词')

    storepath=os.getcwd()+'/Count.txt'  #将结果写到Count.txt文件里，该文件可能需要自助创建
    fp = open(storepath, 'w')
    for i in range(40):
        fp.write(str(list[i]))
        fp.write('\n')

    fp.close




if __name__ == '__main__':

    countfile('File.txt') #输入文件名称（和该文件在同个目录下）
