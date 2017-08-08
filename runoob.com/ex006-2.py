#!/usr/bin/python
#非递归方式实现

def fib(num):
    if num == 0 or num == 1:
        return num
    a,b=0,1
    for i in range(num-1):
        a,b=b,a+b
    return b

for i in range(10):
    print(fib(i))
