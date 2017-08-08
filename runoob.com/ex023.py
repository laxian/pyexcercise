#!/usr/bin/python

# 0   3 * 3
# 1   2 * 2
# 3   1 * 1
# 4   0 * 0

def starLine(long, num):
    star=' '*(int((long-num)/2))
    return star+('*'*num)+star

# 1   2   3   n
# 1   3   5   2*n-1

def printStarLines(n):
    for i in range(1, n+1):
        line=starLine(2*n-1, 2 * i - 1)
        print(line)

    for i in range(n-1, 0, -1):
        line=starLine(2*n-1, 2*i-1)
        print(line)

printStarLines(4)
