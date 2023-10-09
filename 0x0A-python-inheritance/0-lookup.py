#!/usr/bin/python3

"""Module containing a function to lookup the attributes
    and methods of an object
"""

def lookup(obj):
    """
    Get a list of available attributes and methods of an object.

    Parameters:
    obj (object): The object for which you want to retrieve attributes and methods.

    Returns:
    list: A list containing the names of available attributes and methods.
    """

    attributes_and_methods = dir(obj)

    return attributes_and_methods
