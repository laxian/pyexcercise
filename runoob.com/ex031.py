#!/usr/bin/python

def func():
    letter = input('please input：')

    while letter != 'q':
        if letter == 'M':
            print("Monday")
        elif letter == 'T':
            letter = input('input the second letter')
            while letter != 'H' and letter != 'U':
                letter = input('input the second letter')
            if letter == 'H':
                print('Thursday')
            else:
                print('Tuesday')
        elif letter == 'W':
            print("Wednesday")
        elif letter == 'F':
            print('Friday')
        elif letter == 'S':
            letter = input('input the second letter')
            while letter != 'A' and letter != 'U':
                letter = input('input the second letter')
            if letter == 'A':
                print('Saturday')
            else:
                print('Sunday')

        letter = input('please input：')


func()
