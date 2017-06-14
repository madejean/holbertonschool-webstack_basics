#!/usr/bin/python3
import sys

def number_agrv():
    """gets command-line argmuments from script and outputs the number of argmuments"""
    argv = sys.argv[1:]

    if len(argv) == 0:
        print("{} argmument.".format(len(argv)))
    elif len(argv) == 1:
        print("{} argmument:".format(len(argv)))
        for i in argv:
            print("{}: {}".format(len(argv), i))
    else:
        print("{} argmuments:".format(len(argv)))
        for i in range(len(argv)):
            print("{}: {}".format(i + 1, argv[i]))

if __name__ == "__main__":
    number_agrv()
