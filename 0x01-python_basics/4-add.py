#!/usr/bin/python3
add = __import__("add_4").add


def addition():
    """calls the imported add function passing it the value of a and b"""
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(1, 2)))

"""not executing when imported"""
if __name__ == "__main__":
    addition()
