#!/usr/bin/python3
ad = __import__("add_4").add


def addition():
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, ad(1, 2)))

if __name__ == "__main__":
    addition()
