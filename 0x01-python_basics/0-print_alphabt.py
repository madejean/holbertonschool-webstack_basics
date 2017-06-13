#!/usr/bin/python3
"""Prints the entire alphabet except for the letters q and e"""

for i in range(97, 123):
    if i != 113 and i != 101:
        print("{}".format(chr(i)), end="")
