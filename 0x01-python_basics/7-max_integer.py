#!/usr/bin/python3
def max_integer(my_list=[]):
    """returns the max integer from the list"""
    if not my_list:
        return None
    else:
        num = my_list[0]
        for i in my_list:
            if num < i:
                num = i
    return num
