#!/usr/bin/python3
for i in range(0, 100):
    if i < 9:
        print("{}".format(0), end="")
    print("{}".format(i), end=", " if i <= 98 else "\n")
