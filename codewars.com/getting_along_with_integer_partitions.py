from functools import reduce
import time


def part(n):
    lst = shrink(f(n))
    print(lst)
    return "Range: %d Average: %.2f Median: %.2f" % (max(lst)-min(lst),sum(lst)*1.0/len(lst),get_median(list(lst)))

def shrink(lst):
    return set(map(lambda l: reduce(lambda x, y: x * y, l), lst))

def get_median(data):
    data.sort()
    half = len(data) // 2
    return (data[half] + data[~half]) / 2.0

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
        # print(ret)
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
        print(part(6))
        # print(shrink(f(8)))
    print(time.time()-tick)
    # print(f(7))
    # print(dummy([[1,1],[1,2]], 3))
    # print(shrink([[1,2],[2,3]]))
