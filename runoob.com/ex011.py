#!/usr/bin/python


def fib(n):
    if n==1 or n==2:
        return n
    f1 = 1
    f2 = 1
    for i in range(2,n):
        f1,f2=f2,f1+f2
    return f2

for i in range(10):
    print(fib(i))