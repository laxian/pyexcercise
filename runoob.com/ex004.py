#!/usr/bin/python

dayOfMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


while True:
    ans = 0
    year = int(input("input year"))
    print("leap") if is_leap(year) else print("not leap")

    month = 0
    while month < 1 or month > 12:
        month = int(input('month'))
    dayMax = dayOfMonth[month - 1]

    day = 0
    while day < 1 or day > dayMax:
        day = int(input('day'))

    for i in range(0, month):
        ans += dayOfMonth[i]
    ans += day

    print('---%r---'%ans)