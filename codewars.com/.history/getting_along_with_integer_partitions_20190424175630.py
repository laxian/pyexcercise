


def f(n):
    if n == 1:
        return [1]
    ret = []
    for m in range(n, 1):
        print()
        r = min(m, n-m)
        ret.extend(accept(f(r)+[m]))
        print(ret)
    return ret


def accept(lst, n):
    return [x+n for x in list]


if __name__ == '__main__':
    print(f(5))