#!/usr/bin/python3

"""Module containing a function to check if an object's class inherited
(directly or indirectly) from a specified class.
"""

def inherits_from(obj, a_class):
    """Check if the object's class inherited (directly or indirectly) from the
specified class.

    Args:
        obj (object): The object to check.
        a_class (class): The class to compare with.

    Returns:
        bool: True if the object's class inherited (directly or indirectly)
from the specified class, False otherwise.
    """
    return issubclass(type(obj), a_class)
