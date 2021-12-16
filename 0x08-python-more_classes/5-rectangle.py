#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """blueprint of a Rectangle"""
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
        return self.__width

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

    def area(self):
        """A method that calculates the
            area of a rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """A method that calculates the
            perimeter of a rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """a method that prints a rectangle
            with # character
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = []
        for x in range(self.__height):
            [rectangle.append('#') for y in range(self.__width)]
            if x != self.__height - 1:
                rectangle.append("\n")
        return "".join(rectangle)

    def __repr__(self):
        """return a string representation of the rectangle"""
        rectangle = 'Rectangle({}, {})'.format(self.__width, self.__height)
        return rectangle

    def __del__(self):
        """Prints a message when an instance of rextangle has been deleted"""
        print("Bye rectangle...")
