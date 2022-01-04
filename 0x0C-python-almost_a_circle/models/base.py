#!/usr/bin/python3
"""Creating Base class"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""

        filename = cls.__name__ + ".json"
        list_ins = []
        with open(filename, "w", encoding="utf-8") as myfile:
            if list_objs:
                for i in list_objs:
                    list_ins.append(i.to_dictionary())
            myfile.write(cls.to_json_string(list_ins))
