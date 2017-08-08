


numbers = '4 5 29 54 4 0 -214 542 -64 1 -3 6 -6'

def to_sorted_arr(numbers):
    arr = sorted(list(map(lambda i: int(i), [n for n in numbers.split()])))
    return "%d %d"%(arr[0], arr[-1])


print(to_sorted_arr(numbers))
