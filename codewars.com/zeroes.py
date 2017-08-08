
# A problem at https://www.codewars.com/kata/55c4eb777e07c13528000021

def factors(n):
    ret = []
    f = 2
    while n > 1:
        if n % f == 0:
            n /= f
            ret.append(f)
        else:
            f += 1
    return ret


def zeroes(b, n):
    factor=sorted(factors(b))
    fset=list(set(factor))
    all=[]
    for ii in range(2,n+1):
        i=ii
        f=0
        while i>1 and f<len(fset):
            if i%fset[f]==0:
                i//=fset[f]
                all.append(fset[f])
            else:
                f+=1

    if all == []:
        return 0
    l=[x for x in all if x in factor]
    ret=[]
    for f in set(factor):
        ret.append(all.count(f)//factor.count(f))

    return min(ret)

print (zeroes(40, 10))