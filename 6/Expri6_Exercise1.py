# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Expri6_Exercise1
   Description :
   Author :       Adminstrator
   date：          2019/6/10
-------------------------------------------------
   Change Activity:
                   2019/6/10:
-------------------------------------------------
"""

'''
Exercise 1: Prime numbers
Write an iterator that iterates over the first n prime numbers. Use this to print out the
first 10,000 primes.
编写一个迭代器，迭代前n个素数。用这个打印出前1000个素数
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

    print(primelist)

def main():
    printfirstnprime(1000)


if __name__ == '__main__':
    main()

'''
def printfirstnprime(n):
    from collections import Iterator

    cout=0
    primelist=[]
    it=iter([i for i in range(2,100)])
    isbreak=False
    while True:
        try:
           if(cout!=n):
               tempval=next(it)
               for i in range(2,tempval):
                   if(tempval%i==0):

                       break
               else:
                   primelist.append(tempval)
                   cout+=1
           else:
               break
        except StopIteration:
            break

    print(primelist)

def main():
    printfirstnprime(10)
'''