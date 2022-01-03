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
        return self.__size

    @size.setter
    def size(self, value):
        """setter method"""
        self.__size = value
        self.width = self.height = value

    def __str__(self):
        """overiding string method"""
        return "[{}] ({:d}) {:d}/{:d} - {:d}".format(
                __class__.__name__, self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """A method that assigns attributes"""
        attr_arg = [self.id, self.size, self.x, self.y]

        if args:
            for i in range(len(args)):
                attr_arg[i] = args[i]
        else:
            if kwargs:
                for k, v in kwargs.items():
                    if k == "id":
                        attr_arg[0] = v
                    if k == "size":
                        attr_arg[1] = v
                    if k == "x":
                        attr_arg[2] = v
                    if k == "y":
                        attr_arg[3] = v
            else:
                return

        self.__init__(attr_arg[1], attr_arg[2],
                      attr_arg[3], attr_arg[0])

    def to_dictionary(self):
        """Returns a dictionary representation of a Rectangle"""
        obj = {
                "id": self.id,
                "size": self.__size,
                "x": self.x,
                "y": self.y
            }
        return obj
