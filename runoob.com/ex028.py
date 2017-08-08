#!/usr/bin/python

#
p1 = 10
p2 = p1 + 2
p3 = p2 + 2
p4 = p3 + 2
p5 = p4 + 2


def age(n):
    if n == 1:
        return 10
    else:
        return age(n - 1) + 2


print(age(5))
