#!/usr/bin/python

def valueOfN(n, a):
    ans=a
    while n > 1:
        ans*=10
        ans+=a
        n-=1
    return ans

def func(n, a):
    n2=1
    ans=0
    while n2 <= n:
        vi=valueOfN(n2, a)
        print(vi)
        ans+=vi
        n2+=1
    print(ans)


while True:
    n = int(input('input n'))
    a = int(input('input a'))
    vn=valueOfN(n, a)
    print(func(n, a))