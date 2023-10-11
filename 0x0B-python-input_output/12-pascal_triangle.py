#!/usr/bin/python3

"""Module for generating Pascal's triangle"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle for n rows.

    Parameters:
        n (int): The number of rows to generate in the triangle.

    Returns:
        list of lists: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    # Initialize the triangle with the first row containing 1
    triangle = [[1]]

    for i in range(1, n):
        # Calculate the next row based on the previous row
        prev_row = triangle[-1]
        new_row = [1]  # The first element is always 1

        for j in range(1, i):
            new_element = prev_row[j - 1] + prev_row[j]
            new_row.append(new_element)

        new_row.append(1)  # The last element is always 1
        triangle.append(new_row)

    return triangle
