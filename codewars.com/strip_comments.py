
# https://www.codewars.com/kata/strip-comments/train/python
def solution(s, m):
    r = ''
    l = True
    for i in range(len(s)):
        c = s[i]
        print(c)
        if c in m:
            r = r.rstrip(' ')
            l = False
        elif l == True:
            r += c
        elif c == '\n':
            r += c
            l = True
    return r


s = "a #b\nc\nd $e f g"
s = "apples, pears # and bananas\ngrapes\nbananas !apples"
m = ['#', '$']
if __name__ == '__main__':
    print(solution(s, m))
