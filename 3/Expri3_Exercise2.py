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
def getl1(vx,vy):
    aimvalue=0

    for i,val in enumerate(vx):
        aimvalue+=abs(val-vy[i])

    return aimvalue

def getl2(vx,vy):
    import math
    sumvalue=0
    for i,val in enumerate(vx):
        sumvalue+=math.pow(val-vy[i],2)

    return math.sqrt(sumvalue)


def main():
    v_x=(1,3,5,7,9)
    v_y=(2,4,6,8,10)

    print(getl1(v_x,v_y))
    print(getl2(v_x, v_y))
if __name__ == '__main__':
    main()