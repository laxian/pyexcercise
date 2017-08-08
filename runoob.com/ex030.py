#!/usr/bin/python

def func():
    a = str(input('请输入一个5位数'))
    for i in range(int(len(a) / 2)):
        if a[i] != a[-i - 1]:
            return False
    return True


if func():
    print("yes")
else:
    print("no")