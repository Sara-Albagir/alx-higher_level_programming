#!/usr/bin/ python3
def print_last_digit(number):
    if number < 0:
        last = - (abs(number) % 10)
    elif number == 0:
        last = 0
    else:
        last = number % 10
    return last
