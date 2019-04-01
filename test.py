# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test
   Description :
   Author :       Adminstrator
   date：          2019/4/1
-------------------------------------------------
   Change Activity:
                   2019/4/1:
-------------------------------------------------
"""

def main():
    lis = [1,2,3]
    li=[]
    for i in lis:
        li.extend(i)
    print(li)

if __name__ == '__main__':
    main()