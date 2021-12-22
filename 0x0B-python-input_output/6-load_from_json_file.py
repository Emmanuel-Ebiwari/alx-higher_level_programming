#!/usr/bin/python3
"""Creates a function that creates an
    Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """Creates an object from a json file"""
    with open(filename, encoding="utf-8") as myFile:
        json.load(myFile)
