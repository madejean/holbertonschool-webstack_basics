#!/usr/bin/python3
"""Prints the entire alphabet except for the letters q and e"""
for i in range(ord("a"), ord("z") + 1):
    if i != ord("q") and i != ord("e"):
        print("{}".format(chr(i)), end="")
