#!/usr/bin/python3
"""Creates a function that writes an Object
    to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """Writing a json representation of an object
        to a file
    """
    with open(filename, "w", encoding="utf-8") as myFile:
        json.dump(my_obj, myFile)
