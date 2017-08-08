#!/usr/bin/python

a1 = 100
a2 = 268

limit = 10000


def isSqrt(num):
    if num == 1:
        return True
    for i in range(int(num / 2)):
        if i * i == num:
            return True
    return False


for ans in range(10000):
    if isSqrt(ans + a1) and isSqrt(ans + a2):
        print(ans)
