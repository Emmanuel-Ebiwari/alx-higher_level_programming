#!/usr/bin/python3
"""Creates BaseGeometry class"""


class BaseGeometry:
    """A class with a method"""
    def area(self):
        """Raises an Exception with the
            message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A function that validates value"""
        self.name = name
        self.value = value
        if not isinstance(self.value, int):
            raise TypeError("{} must be an integer".format(self.name))
        if self.value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry class"""
    def __init__(self, width, height):
        """initializes width and height properties"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of the class"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)


class Square(Rectangle):
    """inherits from the Rectangle class"""
    def __init__(self, size):
        """initializes the size property"""
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns the area of a square"""
        return self.__size ** 2

    def __str__(self):
        """Returns a string representation of the class"""
        return "[Rectangle] {:d}/{:d}".format(self.__size, self.__size)
