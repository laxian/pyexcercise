#!/usr/bin/python

#判断素数101-200

def prime(num):
    if num==1:return False
    if num==2:return True
    limit=3 if num/2<=2 else num/2

    for i in range(2, int(limit)):
        if num%i==0:
            return False
    return True

for n in range(101, 201):
    if prime(n):
        print(n)