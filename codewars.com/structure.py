
# https://www.codewars.com/kata/520446778469526ec0000001

def same_structure_as(one,two):
    m=one
    n=two
    cur=0
    pre=[]
    while True:
        if type(m)!=type(n):
            return False
        if type(m)==type([]):
            if len(m)!=len(n):
                return False
            else:
                pre.append(m)
                pre.append(n)
                pre.append(cur)
                cur=0
                m=m[cur]
                n=n[cur]
                cur+=1
        else:
            if cur==len(pre[-3]):
                pre.pop()
                pre.pop()
                pre.pop()
                if len(pre)==0:
                    return True
                else:
                    cur=pre[-1]
                    n=pre[-2]
                    m=pre[-3]
                    cur+=1
                    m=m[cur]
                    n=n[cur]
            else:
                n = pre[-2]
                m = pre[-3]
                m=m[cur]
                n=n[cur]
            cur+=1


    return True




print(same_structure_as([1, 1, 1],[2, 2, 2]))