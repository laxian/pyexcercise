
def count_change(money, coins):
    m=money
    c=coins

    cur=0
    pre=[]
    lst=[]
    ret=[]
    while True:
        if cur==len(c):
            break
        n=c[cur]
        if m == n:
            if (lst[-1] if len(lst)>0 else n)>=n:
                print(lst+[n])
                ret.append(lst+[n])
            cur+=1
        elif m>n:
            if (lst[-1] if len(lst)>0 else n)>=n:
                lst.append(n)
                m-=n
                pre.append(cur)
                cur=0
            else:
                cur+=1
        else:
            cur+=1
        while cur>=len(c):
            if len(pre)==0:
                break
            cur=pre.pop()+1
            m+=lst.pop()

    return ret

print(count_change(10,[5,3,2]))