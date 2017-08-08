#!/usr/bin/python

# n       1   2   3   4   5   6   ... n
# f(n)    1   2   3   5   8   13  ... f(n-2)+f(n-1)
# g(n)   2/1 3/2                 ...f(n+1)/f(n)
#
# 求 F(n) = f(2)/f(1)+f(3)/f(2)+...+f(n+1)/f(n)


def f(n):
    if n<2 and n>0:
        return n
    f1=1
    f2=2
    for i in range(2, n+1):
        f1,f2=f2,f1+f2
    return f1


def g(n):
    f1=1
    f2=2
    if n<2 and n>0:
        return f2/f1
    for i in range(2, n+1):
        f1,f2=f2,f1+f2
    return f2/f1

# for i in range(1,90):
#     print(g(i))

def F(n):
    ans=0
    for i in range(1, n+1):
        print(g(i))
        ans+=g(i)
    return ans

print("ans is %s"%F(20))