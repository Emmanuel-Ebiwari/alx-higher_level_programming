#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len1 = len(tuple_a)
    len2 = len(tuple_b)
    if len1 < 2:
        if len1 == 0:
            tuple_a = (0, 0)
        else:
            tuple_a = (tuple_a[0], 0)
    if len2 < 2:
        if len2 == 0:
            tuple_b = (0, 0)
        else:
            tuple_b = (tuple_b[0], 0)

    a = int(tuple_a[0]) + int(tuple_b[0])
    b = int(tuple_a[1]) + int(tuple_b[1])
    new_tuple = (a, b)
    return new_tuple
