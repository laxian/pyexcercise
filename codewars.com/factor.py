
# https://www.codewars.com/kata/54d496788776e49e6b00052f

def factor(num):
    num=abs(num)
    ret=set()
    for i in range(2,num//2+1):
        if is_prime(num):
            ret.add(num)
        elif is_prime(i) and num%i==0:
            ret.add(i)
    return ret

def is_prime(num):
    if num!=2:
        for i in range(2,max(3,num//2)):
            if num%i==0:
                return False
    return True

def factor_set(lst):
    s=set()
    for i in a:
        s.update(factor(i))
    return sorted(s)

def sum_for_list(lst):
    ret=[]
    for i in factor_set(lst):
        sum=0
        for c in lst:
            if c%i==0:
                sum+=c
        ret.append([i,sum])
    return ret

a = [-29804, -4209, -28265, -72769, -31744]
print(sum_for_list(a))
