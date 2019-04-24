from functools import reduce
import time


def shrink(lst):
    return set(map(lambda l: reduce(lambda x, y: x * y, l), lst))

cache = {}
def f(n):
    if n == 0:
        return [[]]
    if n == 1:
        return [[1]]
    ret = []
    for m in range(n, 0, -1):
        r = n - m
        if cache.get(r):
            fr = cache[r]
        else:
            fr = f(r)
            cache[r] = fr
        ret.extend(accept(fr, [m]))
        print(ret)
    return ret


def accept(lst, n):
    return [n + x for x in lst if x ==[] or max(x)<=n[0]]


def dummy(lst, s):
    for l in lst:
        while sum(l) < s:
            l.append(1)
    return lst


if __name__ == "__main__":
    tick = time.time()
    for i in range(1):
        print(len(f(50)))
    print(time.time()-tick)
    # print(f(7))
    # print(dummy([[1,1],[1,2]], 3))
    # print(shrink([[1,2],[2,3]]))
