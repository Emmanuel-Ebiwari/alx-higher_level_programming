#!/usr/bin/python3
def no_c(my_string):
    for c in my_string:
        if c == 'ic' or c == 'C':
            return my_string.translate({ord(c): None})
    return my_string
