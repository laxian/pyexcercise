import math

# https://www.codewars.com/kata/square-into-squares-protect-trees/train/python
def fi(i):
    b = False
    stack = []
    while i > 1 and not b:
        r2 = i ** 2
        n2 = i - 1

        while True:
            if r2 == 0:
                b = True
                break

            if n2 == 0:
                if len(stack) > 0:
                    r2, n2 = stack.pop()
                    n2 -= 1
                else:
                    break

            if n2 == 0:
                continue

            # print('%r, %r\n' % (r2, n2))
            stack.append([r2, n2])
            r2 = r2 - n2 ** 2
            n2 = min(n2 - 1, int(math.sqrt(r2)))

        if b:
            return [x[1] for x in reversed(stack)]
        i -= 1

    return None


# print(stack.map((s)=>s[1]).toList().reversed)


if __name__ == "__main__":
    print(fi(8))
    print(fi(11))
    print(fi(50))
