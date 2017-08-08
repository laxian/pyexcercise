#!/usr/bin/python

# day   f(day)
# 10  1
# 9   3
# 8   8
# ...
# f(day)=(f(day+1)+1)*2
# or
# f(day)=(f(day-1)/2-1)
#
# and
# f(10)=1


day=10
result=1
while day>1:
    result+=1
    result*=2
    day-=1
print(result)