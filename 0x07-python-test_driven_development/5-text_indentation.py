#!/usr/bin/python3
""" a function that prints 2 new lines after a special character """


def text_indentation(text):
    """Prints a text with 2 new lines after special characters
        Args:
            text: inputed string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        print(i, end='')
        if i in [':', '.', '?']:
            print('\n\n', end='')
