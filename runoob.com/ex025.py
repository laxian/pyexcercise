#!/usr/bin/python

def fact(n):
    ans=1
    for i in range(n, 0, -1):
        ans*=i
    return ans

# for i in range(1,9):
#     print(fact(i))

def func(n):
    ans=0
    for i in range(1, n+1):
        ans+=fact(i)
    return ans

print(func(20))