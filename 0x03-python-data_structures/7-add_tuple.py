#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure the tuples have at least 2 elements, filling with 0 if needed
    tuple_a = tuple_a[:2] + (0, 0)
    tuple_b = tuple_b[:2] + (0, 0)

    # Calculate the sum of the elements
    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    return result
