'''
(a)
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            print(" %d 不是质数" % n)
            break
    else:
        print(" %d 是个质数" % n)




def main():
    num=int(input('请输入一个数：'))
    is_prime(num)

-----------------------------------------------------

(b)
def is_prime(n):
    if n>=2:
        if (n == 2) or (n == 3):
            print(n, 'is a prime')

        else:
            if ((n - 1) % 6 == 0) or ((n + 1) % 6 == 0):
                for i in range(2, n):
                    if n % i == 0:
                        print(n, '这不是质数')
                        break
                else:
                    print(n, '这是一个质数')



def main():
    num=int(input('please input a number:'))
    is_prime(num)

----------------------------------------------------------

(c)
def getlistofprime(n):
    primelist=[]
    for i in range(2,n+1):
        if i >= 2:
            if (i == 2) or (i == 3):
                primelist.append(i)

            else:
                if ((i - 1) % 6 == 0) or ((i + 1) % 6 == 0):
                    for j in range(2, i):
                        if i % j == 0:
                            break
                    else:
                        primelist.append(i)

    return primelist

def main():
    num=int(input('Please input the broader of primes:'))
    primelist=getlistofprime(num)
    print(primelist)

----------------------------------------------------------

(d)
def getfirstnprimes(n):
    i=2
    cout=0
    primelist=[]

    while cout!=n:
        if i >= 2:
            if (i == 2) or (i == 3):
                primelist.append(i)
                cout=cout+1

            else:
                if ((i - 1) % 6 == 0) or ((i + 1) % 6 == 0):
                    for j in range(2, i):
                        if i % j == 0:
                            break
                    else:
                        primelist.append(i)
                        cout=cout+1
        i=i+1
    return primelist

def main():
    num=int(input('Please input the the number of primes you want:'))
    primelist=getfirstnprimes(num)
    print(primelist)

'''

if __name__ == '__main__':
    main()


