def f(n):
    if n == 0:
        return [[]]
    if n == 1:
        return [[1]]
    ret = []
    for m in range(n, 0, -1):
        r = min(m, n - m)
        fr = f(r)
        ret.extend(accept(fr, [m]))
        print(ret)
    return ret

def dummy(lst, sum):
    for l in lst:
        while sum(l)<

def accept(lst, n):
    return [n + x for x in lst]


if __name__ == "__main__":
    print(f(5))
