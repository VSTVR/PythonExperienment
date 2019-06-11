# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Expri6_Exercise3
   Description :
   Author :       Adminstrator
   date：          2019/6/10
-------------------------------------------------
   Change Activity:
                   2019/6/10:
-------------------------------------------------
"""

'''
Exercise 3: List comprehensions
Let i, j = 1 ,….., n
(a) Generate a list with elements [i,j].
(b) Generate a list with elements [i,j] with i < j
(c) Generate a list with elements i + j with both i and j prime and i > j.
'''
def printfirstnprime(n):
    from collections import Iterator

    cout=0
    primelist=[]
    tempval=2

    while(cout!=n):
        it=iter([i for i in range(2,tempval)])
        while True:
            try:
                i=next(it)
                if(tempval%i==0):
                    tempval+=1
                    break
            except StopIteration:
                primelist.append(tempval)
                cout+=1
                tempval+=1
                break
    return primelist


def main():

    n=5
    primelist=printfirstnprime(n)
    maxnum=max(primelist)
    lista=[[i,j] for i in range(1,n) for j in range(1,n)]
    listb=[[i,j] for i in range(1,n) for j in range(1,n) if i<j]
    listc=[i+j for i in range(2,maxnum) for j in range(2,maxnum) if i in primelist and j in primelist and i>j ]
    print('lista: ',lista)
    print('listb: ',listb)
    print('primelist: ',primelist)
    print('listc: ',listc)





if __name__ == '__main__':
    main()