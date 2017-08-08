intarr = [2, 6, 8, 10, 3]


def find_outlier(intarr):
    return intarr[list(i % 2 for i in intarr).index(1)] if sum(list(i % 2 for i in intarr)) == 1 else intarr[
        list(i % 2 for i in intarr).index(0)]


print(find_outlier(intarr))

print(intarr[list(i % 2 for i in intarr).index(1)] if sum(list(i % 2 for i in intarr)) == 1 else intarr[
    list(i % 2 for i in intarr).index(0)])
