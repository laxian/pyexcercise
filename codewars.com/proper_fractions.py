from math import sqrt, ceil
import time


# https://www.codewars.com/kata/number-of-proper-fractions-with-denominator-d/train/python
def proper_fractions(n):
    sum = 0
    f = prime_factor(n)
    for i in range(1, n):
        fi = prime_factor(i)
        if fi.intersection(f) == set():
            sum += 1
    return sum


def prime_factor(n):
    f = set()
    limit = int(n / 2) + 1
    for i in range(2, limit):
        if n == 0:
            break
        while n % i == 0:
            if i not in f:
                f.add(i)
            n /= i
    if f == set():
        f.add(n)
    return f



def proper_fractions4(n):
    if n == 1:
        return 0
    sum = n - 1
    f = prime_factor(n)
    if f == set():
        return 1
    for p in f:
        for i in range(1, n):
            if i % p == 0:
                sum -= 1
    return sum

def proper_fractions3(n):
    sum = 0
    f = prime_factor(n)
    for prime in f:
        if n == prime:
            return n - 1
        proper = True
        for i in range(1, n):
            if i % prime == 0:
                proper = False
                break
        if proper:
            sum += 1
    return sum

def proper_fractions2(n):
    sum = 0
    for i in range(1, n):
        if gcd(n, i) == 1:
            sum += 1
    return sum


def gcd(a, b):
    while a % b != 0:
        c = a % b
        a = b
        b = c
    return b


def factor(n):
    r = []
    for i in range(2, int(ceil(sqrt(n))) + 1):
        if gcd(n, i) != 1:
            r.append(i)
    return r


# def gcd(a, b):
#     if a % b == 0:
#         return b
#     return gcd(b, a % b)


if __name__ == '__main__':
    tick = time.time()
    # print(proper_fractions4(1))
    # print(proper_fractions4(2))
    # print(proper_fractions4(5))
    # print(proper_fractions4(15))
    # print(proper_fractions4(25))
    print(proper_fractions3(36))
    print(proper_fractions3(101))
    # for i in range(100):
    #     print(proper_fractions4(152349))
    # print(time.time() - tick)
    # print(proper_fractions(25345678))
# 1 5 7 11 13 17 19 23 29 31 35
    # print(gcd(25,5))
    # print(factor(36))

    # print(prime_factor(2))
    # print(prime_factor(3))
    print(prime_factor(900))
