#!/usr/bin/python3
for i in range(97, 123):
    i = chr(i)
    if i == "e" or i == "q":
        i = ""
    else:
        print("{}".format(i), end="")
