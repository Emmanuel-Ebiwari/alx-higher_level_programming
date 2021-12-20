#!/usr/bin/python3
"""Creates a class MyList that inherits from list"""


class MyList(list):
    """a class that inherits from the list class"""
    def print_sorted(self):
        """Prints a sorted list in ascending order"""
        print(sorted(self))
