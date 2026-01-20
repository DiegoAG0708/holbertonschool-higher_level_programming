#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix
by a given number, returning a new matrix with values rounded to 2 decimals.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div, rounding to 2 decimals.

    Args:
        matrix: list of lists of integers/floats
        div: number (int or float)

    Returns:
        list of lists: new matrix with divided values

    Raises:
        TypeError: if matrix is not a matrix of ints/floats,
                   if rows are not the same size,
                   or if div is not a number
        ZeroDivisionError: if div is zero
    """
    # Validate matrix structure
    if (not isinstance(matrix, list) or
            any(not isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate elements and row sizes
    if len(matrix) == 0 or any(len(row) == 0 for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    # Reject NaN/inf without imports
    if isinstance(div, float) and (div != div or div == float('inf') or div == -float('inf')):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Build new matrix with rounded results
    return [[round(x / div, 2) for x in row] for row in matrix]
