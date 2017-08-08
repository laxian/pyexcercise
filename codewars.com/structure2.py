
# https://www.codewars.com/kata/520446778469526ec0000001

def same_structure_as(one,two):
    if not (type(one)==type([]) and type(two)==type([])):
        if type(one)==type([]) or type(two)==type([]):
            return False
        else:
            return True
    else:
        if len(one)!=len(two):
            return False
        for x in range(0,len(one)):
            i,j=one[x],two[x]
            if not same_structure_as(i,j):
                    return False
        return True



# print(same_structure_as([1, 1, 1],[2, 2, 2,1]))
# print(same_structure_as([1,[1,1]],[2,[2,2]]))
# print(same_structure_as([1, [1, 1]],[[2, 2], 2]))
print(same_structure_as([1, '[', ']'],['[', ']', 1]))