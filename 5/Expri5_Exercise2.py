# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Expri5_Exercise2
   Description :
   Author :       Adminstrator
   date：          2019/5/28
-------------------------------------------------
   Change Activity:
                   2019/5/28:
-------------------------------------------------
"""
'''
Let's implement class which contain some vector functions. There are two types of
vectors, normal or dense vectors, which we can represent using lists. For sparse vectors,
where many of the elements are zero, this is inefficient. Instead, we use a dictionary
with keys the indices of non-zero values, and then the value corresponding to the key
is the value of the vector at that index. Hence, the vector [1; 2; 4] can be stored as a list:
[1, 2, 4] or as a dictionary {0:1, 1: 2, 2: 4}.
we would like to represent sparse and dense vectors as classes, this way we can overload
operators such as + ( add ) and get sensible output. For example, using + on two dense
vectors implemented as lists would append the second vector to the first, instead of
adding the two together.
Implement sparse and dense vectors. Both classes should have the following
capabilities:
(a) Print vector
(b) Add two vectors (both if other is dense and sparse)
(c) Multiply two vectors (both if other is dense and sparse)
Hint: isinstance() might be useful.
'''

class DVector:
    def __init__(self,vector):
       self.value=vector

    def __str__(self):
        return str(self.value)

    def __add__(self, other):
        if isinstance(other.value,list): #dense+dense
            print('dense+dense')
            aimvector = []
            for i, val in enumerate(self.value):
                temp=val + other.value[i]
                aimvector.append(temp)
            return DVector(aimvector)

        elif isinstance(other.value,dict): #dense+sparse
            print('dense+sparse')
            aimvector = []
            for i, val in enumerate(self.value):
                if i in other.value:
                    tempval=val+other.value[i]
                    aimvector.append(tempval)  ###
                else:
                    aimvector.append(val)
            return DVector(aimvector)

    def __mul__(self, other):
        if isinstance(other.value, list):  # dense*dense
            print('dense*dense')
            result=0
            for i,val in enumerate(self.value):
                result+=val*other.value[i]
            return result
        elif isinstance(other.value, dict):  # dense*sparse
            print('dense*sparse')
            result=0
            for i,val in enumerate(self.value):
                if i in other.value:
                    result+=val*other.value[i]
            return result



class SVector:
    def __init__(self,vector):
        self.value=vector

    def __str__(self):
        return str(self.value)

    def __add__(self, other):
        if isinstance(other.value,dict): #sparse+sparse
            print('sparse+sparse')
            tempselfdic={}
            aimdic = {}
            for key, val in other.value.items():
                if key in tempselfdic:
                    tempselfdic[key] += other.value[key]
                else:
                    tempselfdic[key] = val
            aimdic = dict(sorted(tempselfdic.items(), key=lambda x: x[0]))
            return SVector(aimdic)

        elif isinstance(other.value,list): #sparse +dense
            print('sparse +dense')
            aimvector=[]
            for i,val in enumerate(other.value):
                if i in self.value:
                    temp=val+self.value[i]
                    aimvector.append(temp)
                else:
                    aimvector.append(val)
            return DVector(aimvector)

    def __mul__(self, other):
        if isinstance(other.value, dict):  # sparse*sparse
            print('sparse*sparse')
            result=0
            for key,val in self.value.items():
                if key in other.value:
                    result+=val*other.value[key]
            return result

        elif isinstance(other.value, list):  # sparse*dense
            print('sparse*dense')
            result=0
            for i,val in enumerate(other.value):
                if i in self.value:
                    result+=val*self.value[i]
            return result






a=[0,1,2,3]
b=[1,2,3,4]
c={0:100,3:100}
d={1:99,2:99}
a_dns=DVector(a)
b_dns=DVector(b)
c_sps=SVector(c)
d_sps=SVector(d)

print(a_dns*c_sps)
print(d_sps*b_dns)



