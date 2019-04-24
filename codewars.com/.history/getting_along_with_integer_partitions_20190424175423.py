if __name__ == '__main__':
    print('hello')


def f(n):
    if n == 1:
        return [1]
    ret = []
    for m in range(n, 1):
        r = min(m, n-m)
        return accept(f(r)+[m])


def accept(lst, n):
    return [x+n for x in list]