#!/usr/bin/python3
"""Creates a function that returns the JSON
    representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """returns a JSON representation of an object
        Args:
            my_obj: object to be encoded
    """
    return json.dumps(my_obj)
