#!/usr/bin/python

# 递归求阶乘
def fact_r(n):
    if n==1:
        return 1
    else:
        return fact_r(n-1)*n

for i in range(1,6):
    print(fact_r(i))