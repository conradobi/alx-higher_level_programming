#!/usr/bin/python3
def print_last_digit(number):
    last_digit = number % 10
    return last_digit

print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)