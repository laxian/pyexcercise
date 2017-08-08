
# https://www.codewars.com/kata/51675d17e0c1bed195000001

def solution(digits):
    return max([int(''.join(digits[i:i+5])) for i in range(0, len(digits)-5)])

d='1234567898765'

print(solution(d))