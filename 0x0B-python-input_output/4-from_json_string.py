#!/usr/bin/python3
"""Creates a function that returns an object
    (Python data structure) represented by a JSON string
"""
import json


def from_json_string(my_str):
    """Returns an object from a json string"""
    return json.loads(my_str)
