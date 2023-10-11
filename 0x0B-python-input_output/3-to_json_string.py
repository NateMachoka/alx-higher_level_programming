#!/usr/bin/python3

"""Module for converting an object to a JSON string"""


import json


def to_json_string(my_obj):
    """
    Convert an object to a JSON string representation.

    Parameters:
    my_obj (object): The object to be converted to a JSON string.

    Returns:
    str: The JSON representation of the object as a string.
    """
    json_string = json.dumps(my_obj)
    return json_string
