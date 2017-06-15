#!/usr/bin/python3
import sys


def number_argv():
    argv = sys.argv
    if len(argv) < 2:
        print("{} argmument.".format(0))
    elif len(argv) == 2:
        print("{} argmument:".format(1))
        print("{}: {}".format(1, argv[1]))
    else:
        print("{} argmuments:".format(len(argv) - 1))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))

if __name__ == "__main__":
    number_argv()
