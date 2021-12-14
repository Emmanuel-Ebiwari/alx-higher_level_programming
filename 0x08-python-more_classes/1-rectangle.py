#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Creates a rectangle blueprint"""

    def __init__(self, width=0, height=0):
        """Constructor
        Args:
            width: the width of the rectangle
            height: the height of the rectangle
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getter method"""
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        """setter method"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
