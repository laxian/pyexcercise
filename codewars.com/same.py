

a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
# print(False not in list(True if n * n in a2 else False for n in sorted(a1)))
print(list(n*n for n in sorted(a1)))
print(list(sorted(a2)))
print(list(n*n for n in sorted(a1)) == list(sorted(a2)))

print([1,2]==[2,1])