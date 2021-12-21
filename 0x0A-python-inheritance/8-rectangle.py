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
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
