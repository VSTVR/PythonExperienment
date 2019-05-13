# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Expri4_Exercise1
   Description :
   Author :       Adminstrator
   date：          2019/5/13
-------------------------------------------------
   Change Activity:
                   2019/5/13:
-------------------------------------------------
"""

'''
Write a function that opens a file (input: filename), and prints the file line by line
'''

def printfile(filename):
    import os

    path = os.getcwd() +'/'+filename
    content = []

    fp = open(path, 'r')

    content = fp.readlines()

    fp.close

    for i in content:
        print(i)

if __name__ == '__main__':
    printfile('File.txt')
