# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Expri3_Exercise1
   Description :
   Author :       Adminstrator
   date：          2019/4/15
-------------------------------------------------
   Change Activity:
                   2019/4/15:
-------------------------------------------------
"""


def main():
    aimlist=['w','h','a','t','a','r','e','y','o','u','t','a','l','k','i','n','g','a','b','o','u','t']
    list_sort=sorted(aimlist)
    dic={}
    for i in list_sort:
        if i not in dic:
            tempdic={i:1}
            dic.update(tempdic)
        else:
            dic[i]=dic[i]+1

    print(dic)

if __name__ == '__main__':
    main()

'''

'''