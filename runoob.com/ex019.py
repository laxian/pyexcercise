#!/usr/bin/python

# # from ex014 import isPrime
#
# def isPrime(num):
#     if num==1:return False
#     if num==2:return True
#     limit=3 if num/2<=2 else int(num/2)
#
#     for i in range(2, limit):
#         if num%i==0:
#             return False
#     return True
#
# def toPrimeArr(num):
#     arr=[1]
#     while num > 1:
#         if isPrime(num):
#             arr.append(int(num))
#             num/=num
#         limit = 3 if int(num/2)<3 else int(num/2)
#         for i in range(2, limit):
#             if isPrime(i):
#                 if num%i==0:
#                     arr.append(i)
#                     num/=i
#                     break
#
#     return arr
#
# for i in toPrimeArr(28):
#     print(i)

def suoyouyinshu(n):
    mid=int(n/2)
    arr=[1]
    for i in range(2, mid+1):
        if n%i==0:
            arr.append(i)
    return arr

for i in range(2, 1001):
    arr=suoyouyinshu(i)
    if sum(arr)==i:
        print(i)
        for a in arr:
            print(a, end=' ')
        print('')

