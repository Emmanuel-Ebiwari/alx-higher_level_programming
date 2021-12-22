#!/usr/bin/python3
"""creating a function that reads a text file
    (UTF8) and prints it to the stdout
"""


def read_file(filename=""):
    """Reads and prints a file to stdout """
    with open(filename, mode="r", encoding="utf-8") as myFile:
        print(myFile.read(), end="")
