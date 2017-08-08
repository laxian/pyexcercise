#!/usr/bin/python

def score(num):
    if num>=90:
        print('A')
    elif num>=60:
        print('B')
    else:
        print('C')


for i in range(50,99):
    score(i)
