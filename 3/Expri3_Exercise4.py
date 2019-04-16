# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Expri3_Exercise1
   Description :
   Author :       George
   date：          2019/4/15
-------------------------------------------------
   Change Activity:
                   2019/4/16:
-------------------------------------------------
"""

def getkey(dic,aimvalue):

    for key,val in dic.items():
        if val==aimvalue:
            return key

    print('没有找到该值对应的键！')



def main():

    dic={
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5
    }
    value=int(input('请输入一个值：'))
    ans=getkey(dic,value)
    print(ans)
if __name__ == '__main__':
    main()