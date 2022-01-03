#!/usr/bin/python3
"""Creates a Square class that inherits from Rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """init function"""
        super().__init__(size, size, x, y, id)
        self.__size = size

    @property
    def size(self):
        """getter method"""
        return super(Square, self).width

    @size.setter
    def size(self, value):
        """setter method"""
        Square.width.fset(self, value)
