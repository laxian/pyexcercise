def f(n):
    if n == 0:
        return [[]]
    if n == 1:
        return [[1]]
    ret = []
    for m in range(n, 1, -1):
        r = min(m, n - m)
        print("%r %r" % (m, r))
        
        ret.extend(accept(f(r), [m]))
    return ret


def accept(lst, n):
    return [n + x for x in lst]


if __name__ == "__main__":
    print(f(5))
