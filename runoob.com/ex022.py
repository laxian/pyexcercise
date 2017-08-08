#!/usr/bin/python

t1 = ['a', 'b', 'c']
t2 = ['x', 'y', 'z']

# for i in t1:
#     for j in t2:
#         if i == 'a' and j == 'x':
#             pass
#         elif i == 'c' and j in ['x', 'z']:
#             pass
#         else:
#             print("%s VS %s" % (i, j))

for i in t1:
    for j in t1:
        if i != j:
            for k in t1:
                if k != i and k != j:
                    if i!='a' and i!='c' and k!='c':
                        print("%s--x; %s--y; %s--z"%(i,j,k))