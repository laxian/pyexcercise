def f(n):
    if n == 0:
        return [[]]
    if n == 1:
        return [[1]]
    ret = []
    for m in range(n, 0, -1):
        # r = min(m, n - m)
        r = n - m
        fr = f(r)
        ret.extend(accept(fr, [m]))
        print(ret)
    return set(dummy(ret, n))

def dummy(lst, s):
    for l in lst:
        while sum(l)<s:
            l.append(1)
    return sorted lst

def accept(lst, n):
    return [n + x for x in lst]


if __name__ == "__main__":
    print(f(5))
    # print(f(7))
    # print(dummy([[1,1],[1,2]], 3))
