def f(n):
    if n == 0:
        return []
    if n == 1:
        return [1]
    ret = []
    for m in range(n, 1, -1):
        r = min(m, n - m)
        print("%r %r" % (m, r))
        lst = f(r)
        add = [m]
        ret.extend(accept(lst, add))
    return ret


def accept(lst, n):
    return [x + n for x in list]


if __name__ == "__main__":
    print(f(5))
