#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        dividend = a / b
    except (TypeError, ZeroDivisionError):
        dividend = None
    finally:
        print("Inside result: {}".format(dividend))
    return dividend
