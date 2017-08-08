
# https://www.codewars.com/kata/541af676b589989aed0009e7

def count_change(money, coins):
    if len(coins) == 0:
        return
    if money < min(coins):
        return
    ret=[]
    # print('%s,%s'%(money, coins))
    v = money
    lst = coins
    pre = []
    while v >= min(lst):
        found=False

        print(v,lst)
        for i in lst:
            if v-i in lst:
                print([v-i,i]+pre)
                ret.append(sorted([v-i,i]+pre))
            elif v%i==0:
                print([i for x in range(0,v//i)]+pre)
                ret.append(sorted([i for x in range(0,v//i)]+pre))
        for i in lst:
            found=True
            pre.append(i)
            v=v-i
            break
        if not found:
            break
    ret_s=[]
    for l in ret:
        ret_s.append(fun(l))
    ret_i=[]
    for l in set(ret_s):
        ret_i.append(fun2(l))

    print('----\n')
    print(len(ret_i))
    return ret_i

def fun2(str):
    ret=[]
    for c in str:
        ret.append(int(c))
    return ret


def fun(lst):
    ret=''
    for i in lst:
        ret+=str(i)
    return ret



tmp=0
# count_change(10,[5,3,2])
# count_change(4,[1,2])
# count_change(11,[5,7])
# count_change(10,[1,2,3,4])
# count_change(10,[2,3,5,1])
# print(count_change(10,[5,2,3]))
print(count_change(300,[5, 10, 20, 50, 100, 200, 500]))
# 1111111111
# 111111112
# 11111113
# 111115
# 22111111
# 2221111
# 2311111
# 222211
# 223111
# 331111
# 22222
# 22231
# 33211
# 3322
# 3331
# 5221
# 532

# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# [2, 1, 1, 1, 1, 1, 1, 1, 1]
# [3, 1, 1, 1, 1, 1, 1, 1]
# [5, 1, 1, 1, 1, 1]
# [2, 2, 1, 1, 1, 1, 1, 1]
# [2, 3, 1, 1, 1, 1, 1]
# [2, 2, 2, 2, 2]
# [2, 5, 1, 1, 1]
# [2, 2, 2, 1, 1, 1, 1]
# [2, 2, 2, 2, 1, 1]
# [3, 3, 1, 1, 1, 1]
# [3, 5, 1, 1]
# [3, 3, 3, 1]
# [5, 1, 1, 1, 1, 1]
# [5, 5]

