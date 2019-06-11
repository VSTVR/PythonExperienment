# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Expri6_Exercise2
   Description :
   Author :       Adminstrator
   date：          2019/6/10
-------------------------------------------------
   Change Activity:
                   2019/6/10:
-------------------------------------------------
"""

'''
Exercise 2: Prime challenge
Write the function primes(n) that return a list with all prime numbers up to n
Use lambda functions and list comprehensions.
Try your best to complete it with as little code as possible
'''

def primes(n,end):
    unprimelist_func = lambda x: [y for y in range(2, x) if x % y == 0] #
    primelist = [x for x in range(n,end) if not unprimelist_func(x)] #不知道为什么改成 if x not in ...就会无效

    return primelist

def main():
    n=10   #开始位置
    end=30 #结束位置
    aimlist=primes(n,end)
    print(aimlist)



if __name__ == '__main__':
    main()