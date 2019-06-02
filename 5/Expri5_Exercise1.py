# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Expri5_Exercise1
   Description :
   Author :       Adminstrator
   date：          2019/5/28
-------------------------------------------------
   Change Activity:
                   2019/5/28:
-------------------------------------------------
"""

'''
In this problem, we will write a class that can represent rational numbers, i.e. fractions
p/q.
√(a) Create a class Rational which is initialized by two integers, p and q, the nominator
and denominator
√(b) Add a method to print the rational number as p/q (the __str__ or __repr__ method
is useful).
√(c) We would like to represent 10/20 by 1/2 instead, hence write a function that
computes the greatest common divisor, and ensure that every rational number is
simplified
√(d) Add a method so that we can add two rational numbers with r1 + r2, here the
__add__() method is useful.
√(e) Add a method to subtract two rational numbers. (__sub__)
√(f) Add a method to multiply two rational numbers. (__mul__)
√(g) Add a method to divide two rational numbers. (__truediv__)
√(h) Add a method that compares whether two rational numbers are equal.
(i) Add a method to convert the rational number to a floating point (the __float__()
method maybe handy)
'''

class Fraction:
    def __init__(self,p,q):
        self.nominator=p
        self.denominator=q
        self.normalize()


    def __str__(self):
        return str(self.nominator)+'/'+str(self.denominator)

    def __add__(self,other):
        a = self.nominator
        b = self.denominator
        c = other.nominator
        d = other.denominator
        p = a * d + c * b
        q = b * d
        return Fraction(p,q)

    def __sub__(self,other):
        a = self.nominator
        b = self.denominator
        c = other.nominator
        d = other.denominator
        p=a*d-c*b
        q=b*d
        return Fraction(p,q)

    def __mul__(self,other):
        a = self.nominator
        b = self.denominator
        c = other.nominator
        d = other.denominator
        p=a*c
        q=b*d
        return Fraction(p,q)

    def __truediv__(self,other):
        a = self.nominator
        b = self.denominator
        c = other.nominator
        d = other.denominator
        p=a*d
        q=b*c
        return Fraction(p,q)

    def __eq__(self, other):
        return self.nominator== other.nominator and self.denominator==other.denominator

    def __float__(self):
        return float(self.nominator/self.denominator)


    def normalize(self):
        def gcd(p,q):
            r = 1
            r = p % q
            if r == 0:
                return q
            else:
                return gcd(q, r)
        divide=gcd(self.nominator,self.denominator)
        self.nominator=int(self.nominator/divide)
        self.denominator=int(self.denominator/divide)



a=Fraction(10,20)
b=Fraction(10,30)
c=Fraction(10,20)
print(a,b)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a==b,a==c)
print(float(a),float(b))

