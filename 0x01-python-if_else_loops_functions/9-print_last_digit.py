#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
    print(number % 0, end='')
    return(number % 10)
