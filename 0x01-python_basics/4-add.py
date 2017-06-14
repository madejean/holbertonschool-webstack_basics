#!/usr/bin/python3
add = __import__("add_4").add


def addition():
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(1, 2)))

"""not executing when imported"""
if __name__ == "__main__":
    addition()
