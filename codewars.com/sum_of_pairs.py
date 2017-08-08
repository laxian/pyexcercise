
# https://www.codewars.com/kata/54d81488b981293527000c8f

def sum_pairs(ints ,s):
    print(ints)
    print(s)
    l=len( ints)
    i=0
    j=1
    while j<=l-1 and i<=l-2:
        if ints[i]+ints[ j ]==s:
            print([ints[i],ints[ j]])
            return [ints[i],ints[ j]]
        if i+1<j:
            i+=1
        else:
            j+=1
            i=0
    return None

ints=[20, -13, 40]

def sum_pairs2(ints, s):
    for i in range(1, len(ints)):
        for j in range(0, i):
            if ints[i]+ints[j]==s:
                return [ints[j],ints[i]]
    return None

sum_pairs(ints, -7)