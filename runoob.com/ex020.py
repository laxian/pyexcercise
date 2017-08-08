#!/usr/bin/python

# 1   100     100
# 2   50      150
# 3   25      175
# ...
# n   100*(2**(1-n))  ?

def itemN(n):
    return 100*(2**(1-n))

s10=0
for i in range(1, 11):
    s10+=itemN(i)
print(s10)

print(itemN(11))