#!/usr/bin/python3
def print_last_digit(number):
    number = str(number)
    return number[-1]
    if number >= 0:
        ld = number % 10
    else:
        ld = number % -10
        ld *= -1

    print("{:d}".format(ld), end='')
    return ld