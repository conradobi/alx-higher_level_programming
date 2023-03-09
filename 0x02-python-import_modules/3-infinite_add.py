#!/usr/bin/python3
import sys

"""arg_v = ['./3-infinite_add.py', '79', '10']
sum = int(arg_v[1]) + int(arg_v[2])
print(sum)

print(arg_v)
"""
arg_str = sys.argv
for i in range(len(arg_str)):
    arg_sum = int(arg_str[i]) + i
    print(arg_sum)
