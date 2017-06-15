#!/usr/bin/python3
import doctest

"""
add_integer(a, b) only accepts a and b as integers or floats
a TypeError message will appear if a and b not int or flot
This function returns the addition of a and b as int
"""


def add_integer(a, b):

    """
    returns the addition of a and b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))


if __name__ == '__main__':
    doctest.testfile('./tests/13-add_integer.txt')
