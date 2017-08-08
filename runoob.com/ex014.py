#!/usr/bin/python

def isPrime(num):
    if num==1:return False
    if num==2:return True
    limit=3 if num/2<=2 else int(num/2)

    for i in range(2, limit):
        if num%i==0:
            return False
    return True


def zhishufenjie(num):
    while num > 1:
        if isPrime(num):
            print(int(num))
            num/=num
        limit = 3 if int(num/2)<3 else int(num/2)
        for i in range(2, limit):
            if isPrime(i):
                if num%i==0:
                    print(i)
                    num/=i
                    break

zhishufenjie(513239)