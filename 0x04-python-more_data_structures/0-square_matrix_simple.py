#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        new = []
        for rows in matrix:
            new.append(list(map(lambda x: x**2, rows)))
        return (new)
    return None
