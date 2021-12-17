#!/usr/bin/python3


def add_integer(a, b=98):
    """A function that performs an addition
    Args:
        a: first integer
        b: second integer
    Returns:
        returns the sum of a and b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
