#!/usr/bin/python





def stat(str):
    letter = 0
    space = 0
    digit = 0
    other = 0
    for c in str:
        if c > 'A' and c < 'z':
            letter+=1
        elif c > '0' and c < '9':
            digit+=1
        elif c.isspace():
            space+=1
        else:
            other+=1
    return letter,space,digit,other



str='begin'
while str != 'q':
    print(str)
    str=input("input a string\n")
    print(stat(str))