# https://www.codewars.com/kata/how-many-numbers-iii/train/python
def find_all(sum_dig, digs, minimal=None):
    lst = [int(x) for x in find_all_list(sum_dig, digs)]
    return [len(lst), min(lst), max(lst)] if lst else []

def find_all_list(sum_dig, digs, minimal=None):
    if digs == 1:
        return str(sum_dig) if sum_dig < 10 else None
    result = []
    minimal = minimal if minimal else 1
    for i in range(minimal, sum_dig // digs + 1):
        s = find_all_list(sum_dig - i, digs - 1, i)
        if isinstance(s, list):
            ret = ["%r%s" % (i, c) for c in s]
            result.extend(ret)
        elif s:
            ret = "%r%s" % (i, s)
            result.append(ret)
    return result


if __name__ == "__main__":
    print(find_all(84, 4))
