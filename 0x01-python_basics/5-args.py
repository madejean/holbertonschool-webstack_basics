#!/usr/bin/python3
import sys


def number_agrv():
    """outputs the number of argmuments passed from command-line"""
    argv = sys.argv[1:]
    len_argv = len(argv)
    if len_argv == 0:
        print("{} argmument.".format(len_argv))
    elif len(argv) == 1:
        print("{} argmument:".format(len_argv))
        for i in argv:
            print("{}: {}".format(len_argv, i))
    else:
        print("{} argmuments:".format(len_argv))
        for i in range(len_argv):
            print("{}: {}".format(i + 1, argv[i]))

if __name__ == "__main__":
    number_agrv()
