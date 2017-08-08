#!/usr/bin/python

def prt(d):
    sum = 0
    while d:
        sum+=1
        a=d%10
        d=int(d/10)
        print(a)
    print(sum,"位")


while True:
    prt(int(input("input...")))