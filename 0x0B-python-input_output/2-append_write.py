#!/usr/bin/python3
"""Creates a function that appends a string to a text file
    (UTF8) and returns the number of characters written
"""


def append_write(filename="", text=""):
    """Appends to a file and returns the number of characters written"""
    with open(filename, mode="a", encoding="utf-8") as myFile:
        myFile.write(text)
    with open(filename, encoding="utf-8") as myFile:
        return len(myFile.readline())
