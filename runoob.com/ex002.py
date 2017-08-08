#!/usr/bin/python
# -*- coding: UTF-8 -*-

rat = [0.01,0.015,0.03,0.05,0.075,0.1]
arr = [1000000,600000,400000,200000,100000,0]

while True:
    result = 0
    i = int(input('净利润:'))
    for index in range(len(arr)):
        if(i>arr[index]):
            delta = i - arr[index]
            result += delta*rat[index]
            i-=delta

    print(result)
