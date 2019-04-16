# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Expri3_Exercise1
   Description :
   Author :       George
   date：          2019/4/15
-------------------------------------------------
   Change Activity:
                   2019/4/15:
-------------------------------------------------
"""


def main():

    v_d_a=[1,3,5,7,9,11]
    v_d_b=[2,4,6,8,10,12]

    v_s_a = {0: 11, 2: 11, 5: 11}
    v_s_b = {0: 11, 1: 11, 6: 11}

    print('finish')

if __name__ == '__main__':
    main()



'''
(a)
def addDenseVector(va, vb):

    aimvector=[]
    for i,val in enumerate(va):
        aimvector.append(val+vb[i])

    return aimvector

(b)
def multiDenseVector(va, vb):

    aimvalue=0
    for i,val in enumerate(va):
        aimvalue=aimvalue+(val*vb[i])

    return aimvalue
    
(c)
def addSparseVector(va,vb):
    aimdic={}

    for key,val in vb.items():
        if key in va:
            va[key]+=vb[key]
        else:
            va[key]=val

    aimdic=dict(sorted(va.items(),key=lambda x:x[0]))
    return aimdic
    
(d)
def multiSparseVector(va, vb):
    aimvalue=0

    for key,val in vb.items():
        if key in va:
            aimvalue+=va[key]*val

    return aimvalue
    
(e)
def addDanSVector(va, vb):
    aimvector={}

    for i,val in enumerate(vb):
        if i in va:
            va[i]+=val
        else:
            va[i]=val

    aimvector=dict(sorted(va.items(),key=lambda x:x[0]))
    return aimvector
    
(f)
def multiDanSVector(va, vb):
    aimvalue=0

    for i,val in enumerate(vb):
        if i in va:
            aimvalue+=va[i]*val

    return aimvalue
'''