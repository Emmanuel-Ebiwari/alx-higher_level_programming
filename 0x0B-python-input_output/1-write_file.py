#!/usr/bin/python3
"""Creates a function that writes a string to a text file
    (UTF8) and returns the number of characters written
"""


def write_file(filename="", text=""):
    """Writes to a file and returns the number of characters written"""
    with open(filename, mode="w", encoding="utf-8") as myFile:
        myFile.write(text)
    with open(filename, encoding="utf-8") as myFile:
        return len(myFile.read())
