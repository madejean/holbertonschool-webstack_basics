#!/usr/bin/python3

"""Prints the entire alphabet except for the letters q and e """

for i in range(ord("a"), ord("z")):
    """iterates from a to z not printing q and e"""
    if i != ord("q") and i != ord("e"):
        """does not print a new line"""
        print("{}".format(chr(i)), end="")
