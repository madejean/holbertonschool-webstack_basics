#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    try:
        result = a / b
        result = float("{0:.2f}".format(result))
    except ZeroDivisionError:
        result = None
        return result
    finally:
        print("Inside result: {}".format(result))
        return result
