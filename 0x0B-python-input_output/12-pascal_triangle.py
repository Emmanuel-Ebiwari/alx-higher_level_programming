#!/usr/bin/python3
"""Creates a function that returns a list of lists of integers
    representing the Pascal’s triangle
"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
        the Pascal's triangle
    """
    if n <= 0:
        return []

    my_list = []
    for i in range(n):
        tmp = []
        for j in range(i+1):
            if j == 0 or j == i:
                tmp.append(1)
            else:
                tmp.append(my_list[i-1][j-1] + my_list[i-1][j])
        my_list.append(tmp)
    return my_list
