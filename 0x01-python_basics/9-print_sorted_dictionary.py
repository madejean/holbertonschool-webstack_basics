#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    s = sorted(my_dict.keys())
    for key in s:
        print("{}: {}".format(key, my_dict[key]))
