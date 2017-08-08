#!/usr/bin/python


def shuixianhua(num):
    if num<100 or num>999:
        return False
    bw=int(num/100)
    sw=int(num%100/10)
    gw=num%10
    if bw**3+sw**3+gw**3 == num:
        print(num)
        return True
    return False

for i in range(100,1000):
    shuixianhua(i)