#!/usr/bin/python3
"""Creates a Rectangle clas that inherits from Base class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter method"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter method"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter method"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter method"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """A method that calculates the
            area of a rectangle
        """
        return self.__width * self.__height

    def display(self):
        """Prints out the Rectangle instance with the character #"""

        if self.__width == 0 and self.__height == 0:
            print()

        if self.__y != 0:
            print("\n" * self.__y, end="")
        for i in range(self.__height):
            if self.__x != 0:
                print(" " * self.__x, end="")
            print('#' * self.__width)

    def __str__(self):
        """Returns a given string"""
        return "[{}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
                __class__.__name__, self.id, self.__x,
                self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        attr_arg = [self.id, self.__width, self.__height, self.__x, self.__y]

        if args:
            for i in range(len(args)):
                attr_arg[i] = args[i]
        else:
            if kwargs:
                for k, v in kwargs.items():
                    if k == "id":
                        attr_arg[0] = v
                    if k == "width":
                        attr_arg[1] = v
                    if k == "height":
                        attr_arg[2] = v
                    if k == "x":
                        attr_arg[3] = v
                    if k == "y":
                        attr_arg[4] = v
            else:
                return

        self.__init__(attr_arg[1], attr_arg[2],
                      attr_arg[3], attr_arg[4], attr_arg[0])
