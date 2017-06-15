#!/usr/bin/python3
def no_c(str):
    str_no_c = ""
    for i in str:
        if i != "c" and i != "C":
            str_no_c += i
        else:
            pass
    return str_no_c
