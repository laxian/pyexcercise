
# https://www.codewars.com/kata/556deca17c58da83c00002db

def tribonacci(signature,n):
    if n <= 3:
        return signature[:n]
    lst=list(signature)
    a,b,c=lst[:3]
    for i in range(0, n//3):
        a,b,c = a+b+c,(a+b+c)+b+c,a+b+c+(a+b+c)+b+c+c
        lst.append(a)
        lst.append(b)
        lst.append(c)
    return lst[:n]


sig = [1,1,1]
print(tribonacci(sig, 20))
print(len(tribonacci(sig, 20)))
