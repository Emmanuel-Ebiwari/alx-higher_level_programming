#!/usr/bin/python3
"""Creates an empty class BaseGeometry"""


class BaseGeometry:
    """A class with a method"""
    def area(self):
        """Raises an Exception with the
            message area() is not implemented
        """
        raise Exception("area() is not implemented")
