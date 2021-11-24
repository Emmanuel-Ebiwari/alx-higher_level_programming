#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix[:]
    for x in range(len(new_matrix)):
        for y in range(len(new_matrix[x])):
            new_matrix[x][y] = new_matrix[x][y]**2
    return new_matrix
