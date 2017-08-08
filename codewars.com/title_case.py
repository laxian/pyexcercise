
a = 'THE WIND IN THE WILLOWS'
b = 'The In'
a = 'ab'
b = 'ab'

# m= list(word[0].upper()+word[1:] for word in a.split())[1:]
# n= list(word[0].upper()+word[1:] if word==a.split()[0] or word.lower() not in b.lower().split() else word for word in a.split())
#
# print(m)
# print(n)
#
# print(list(
#     w[0].lower()+w[1:] if w.lower() in b.lower().split() else w for w in m)
# )


# def fun(a,b=''):
#     return list(word[0].upper()+word[1:] if word==a.split()[0] or word.lower() not in b.lower().split() else word for word in a.split())
# def fun(a,b=''):
#     return ''.join(a.split()[0].upper()+a.lower().split()[1:]) + ' ' + ' '.join(list(word if word in b.lower().split() else word[0].upper()+word[1:] for word in a.lower().split()[1:]))
#
# print(fun(a,b))

print(a[0].upper()+a.lower().split()[0][1:])
print(list(a[0].upper()+a.lower().split()[0][1:]).append(list(word.lower() if word in b.lower().split() else word[0].upper()+word[1:] for word in a.lower().split()[1:])))