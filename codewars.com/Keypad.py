
# https://www.codewars.com/kata/54a2e93b22d236498400134b

def presses(phrase):
    str = {"1", "abc2", "def3", "ghi4", "jkl5", "mno6", "pqrs7", "tuv8", "wxyz9", "*", " 0", "#"}

    count = 0
    for c in phrase.upper():
        for s in str:
            S=s.upper()
            if S.find(c) != -1:
                count+=S.find(c)+1
    return count

print(presses("abcdefg"))