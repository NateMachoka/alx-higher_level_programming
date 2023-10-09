#!/usr/bin/python3

"""Module containing a function to check if an object is an instance of a
specified class.
"""


def is_same_class(obj, a_class):
    """Check if the object is exactly an instance of the specified class.

    Args:
        obj (object): The object to check.
        a_class (class): The class to compare with.

    Returns:
        bool: True if the object is exactly an instance of the specified class
    """
    return type(obj) is a_class
