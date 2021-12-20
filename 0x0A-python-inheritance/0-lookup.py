#!/usr/bin/python3
"""A function that returns the list of available
    attributes and methods of an object
"""


def lookup(obj):
    """Returns a list of attributes and methods of
        object using the dir function
        Args:
            obj: object to be checked
    """
    return dir(obj)
