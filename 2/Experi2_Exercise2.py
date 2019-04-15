
def set_first_element_to_zero(list_in):
    list_in[0]=0
    return list_in

def main():
    list_test=[1,2,3,4]
    list_test=set_first_element_to_zero(list_test)
    print(list_test)
if __name__ == '__main__':
    main()

'''a=[{'A':'万其伟'},{'B':'2017222021'},{'C':'生工01'}]
    b=a
    b[1]={'???':'???'}
    c=a[:]
    c[2]={'123':'456'}
    print(a)
'''