
# https://www.codewars.com/kata/55c45be3b2079eccff00010f

sentence = "is2 Thi1s T4est 3a"


def order(sentence):
    print(word.split('') for word in [s for s in sentence.split()])

print([s for s in sentence.split()])
# print(list(
#     list(filter(lambda c: c!='', list((c if c.isdigit() else '' for c in word)))) for word in [s for s in sentence.split()]
# )
# )
#
# print(
#     sorted(
#         list((c if c.isdigit() else '' for c in word)) for word in [s for s in sentence.split()]
#     )
# )

def get_digit(word):
    return int(tuple(filter(lambda i: i.isdigit(), list(c for c in word)))[0])

def cmp(word1, word2):
    return get_digit(word1)>get_digit(word2)

print(' '.join(sorted([s for s in sentence.split()], key=lambda i: sorted(i))))