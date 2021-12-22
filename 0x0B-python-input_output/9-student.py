#!/usr/bin/python3
"""A class Student that defines a student"""


class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        """init function"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
