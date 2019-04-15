def Collatz(n):
    if n%2==0:
        return n//2
    elif n%2==1:
        return (n*3+1)

def getCollatzlist(n):
    list_test = []
    list_test.append(n)
    temp = Collatz(n)
    while temp != 1:
        list_test.append(temp)
        temp = Collatz(temp)

    list_test.append(1)

    return list_test


def getthelongest(n):
    maxlen=0
    maxlist=[]

    for i in range(1,n):
        templist=getCollatzlist(i)
        length=len(templist)
        if length>maxlen:
            maxlen=length
            maxlist=templist

    print('The max length: ',maxlen)
    print('The max list: ',maxlist)



def main():
    n=int(input('请输入n的值'))
    getthelongest(n)

if __name__ == '__main__':
    main()

'''
(a)
def Collatz(n):
    if n%2==0:
        return n//2
    elif n%2==1:
        return (n*3+1)

def getCollatzlist(n):
    list_test = []
    list_test.append(n)
    temp = Collatz(n)
    while temp != 1:
        list_test.append(temp)
        temp = Collatz(temp)

    list_test.append(1)

    return list_test

def main():
    n=int(input('请输入n的值：'))
    list_test=getCollatzlist(n)
    print(list_test)
    
-------------------------------------    

(b)



'''