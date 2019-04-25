# https://www.codewars.com/kata/how-many-numbers-iii/train/python
def find_all(sum_dig, digs, limit=None):
    ret = []
    limit = limit if limit else 9
    if sum_dig > digs*limit or sum_dig < digs:
        return []
    if digs == 1:
        return [sum_dig] if not limit or limit >= sum_dig else []
    if sum_dig == digs:
        return [1] * digs

    if sum_dig < 9:
        lst = [sum_dig-digs+1] + [digs-1]
    else:
        lst = [9]*(sum_dig//9) + [sum_dig%9]
    # print(lst)
    while lst:
        curr = lst.pop()
        print(curr)
        while lst[-1] > 0:
            pre = lst[-1] if lst else None
            sub = find_all(curr, digs - len(lst), pre)
            if sub:
                print(lst)
                print(lst+sub)
                ret.append(lst+sub)
                # return lst + sub
            if pre:
                lst[-1] -= 1
                curr = sum_dig - sum(lst)
        lst.pop()
    return ret


if __name__ == '__main__':
    print(find_all(10, 3))
