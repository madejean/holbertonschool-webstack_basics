#!/usr/bin/python3
for i in range(00, 100):
    if i != 99:
        print("{}".format("%02d" % i), end=", ")
    else:
        print("{}".format(i), end="\n")