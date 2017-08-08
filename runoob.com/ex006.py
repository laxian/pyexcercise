#!/usr/bin/python

def fib(num):
    if num == 0 or num == 1:
        return num
    return fib(num-1)+fib(num-2)

for i in range(10):
    print (fib(i))