
# A problem at https://www.codewars.com/kata/55c4eb777e07c13528000021

def fac(n):
    f, i = 1, 1
    while i <= n:
        f *= i
        i += 1
    return f


def fac2(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


def prime(n):
    m = n / 2
    f = 2
    while f <= m:
        if n % f == 0:
            return False
        f += 1
    return True


def prime_factor(n):
    m = n / 2
    f = 2
    ret = []
    while f <= m:
        if n % f == 0 and prime(f):
            ret.append(f)
        f += 1
    return ret


def div(n):
    ret = []
    factor = prime_factor(n)
    while n > 1:
        for f in factor:
            if n % f == 0:
                ret.append(f)
                n /= f
    return ret


def div2(n):
    ret = []
    f = 2
    while n > 1:
        if n % f == 0:
            n /= f
            ret.append(f)
        else:
            f += 1
    print(ret)
    return ret


# fixme
def zeroes(b, n):
    factor=div2(b)
    i=0
    arr=list(range(1,n+1))
    for a in range(1,n):
        arra=arr[a]
        while arra > 1:
            if arra % factor[i % len(factor)] == 0:
                arr[a] //= factor[i % len(factor)]
                arra //= factor[i % len(factor)]
                i += 1
            else:
                if a+1<n:
                    arr[a+1]*=arra
                break
    return i//len(factor)


print (zeroes(12, 26))