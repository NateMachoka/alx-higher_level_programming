#!/usr/bin/python3

"""Module containing a function to check if an object is an instance of, or
inherited from, a specified class.
"""


def is_kind_of_class(obj, a_class):
    """Check if the object is an instance of, or inherited from, the specified
class.

    Args:
        obj (object): The object to check.
        a_class (class): The class to compare with.

    Returns:
        bool: True if the object is an instance of, or inherited from, the
specified class, False otherwise.
    """
    return isinstance(obj, a_class)
