#!/usr/bin/python

# 递归逆序字符串
def reverse_r(str):
    slen=len(str)
    if slen==1:
        return str
    else:
        return str[slen-1]+reverse_r(str[:slen-1])

while True:
    str=input('input a string')
    print(reverse_r(str))