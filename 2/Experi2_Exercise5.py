
def ai(x,ys):
    newlist=[]
    for i in ys:
        if i<x:
            newlist.append(i)
    newlist.append(x)
    for i in ys:
        if i >=x:
            newlist.append(i)

    print(newlist)



def main():
    import random
    ys=[i for i in range(10)]
    random.shuffle(ys)
    print(ys)
    x=int(input('please input the value of x:'))
    ai(x,ys)


if __name__ == '__main__':
    main()