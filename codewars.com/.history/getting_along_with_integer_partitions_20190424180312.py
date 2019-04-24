def f(n):
    print("begin %r" % n)
    if n == 1:
        return [1]
    ret = []
    for m in range(n):
        r = min(m, n - m)
        print("%r %r" % (m, r))
        ret.extend(accept(f(r) + [m]))
        print(ret)
    return ret


def accept(lst, n):
    return [x + n for x in list]


if __name__ == "__main__":
    print(f(5))
