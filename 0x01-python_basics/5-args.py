#!/usr/bin/python3
import sys

args = sys.argv[1:]

if len(args) == 0:
    print("{} argmument.".format(len(args)))
elif len(args) == 1:
    print("{} argmument:".format(len(args)))
    for i in args:
        print("{}: {}".format(len(args), i))
else:
    print("{} argmuments: ".format(len(args)))
    for i in range(len(args)):
        print("{}: {}".format(i + 1, args[i]))
