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
    unprimelist_func=lambda x:[y for y in range(2,x) if x % y ==0]
    primelist=[x for x in range(2,20) if not unprimelist_func(x)]
    print(primelist)
if __name__ == '__main__':
    main()

'''
优秀
n=10
list=[x for x in range(1, 10) if not[y for y in range(2, x) if x % y == 0]]
    print(list)
'''