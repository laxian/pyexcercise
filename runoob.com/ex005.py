#!/usr/bin/python

list = []

def sort(l):
    for i in range(len(l)):
        for j in range(i, len(l)):
            if l[i]>l[j]:
                l[i]+=l[j]
                l[j]=l[i]-l[j]
                l[i]=l[i]-l[j]

for i in range(3):
    a = int(input('input a num'))
    list.append(a)

# sort(list)
list.sort()

print(list)