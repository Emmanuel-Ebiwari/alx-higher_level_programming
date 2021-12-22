#!/usr/bin/python3
"""Creates a function that returns the dictionary
    description with simple data structure for JSON
    serialization of an object
"""


def class_to_json(obj):
    """returns the dictionary description of obj"""
    return obj.__dict__
