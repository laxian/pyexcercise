#!/usr/bin/python

cnt = 0
for i in range(1,5):
    for j in range(1,5):
        if(j == i):
            continue
        for k in range(1, 5):
            if(k == j or k == i):
                continue
            print(i, j, k)
            cnt += 1
print(cnt)
