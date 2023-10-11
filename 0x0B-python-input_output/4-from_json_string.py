#!/usr/bin/python3

"""Module for converting a JSON string to a Python object"""


import json


def from_json_string(my_str):
    """
    Convert a JSON string to a Python data structure (object).

    Parameters:
    my_str (str): The JSON string to be converted to a Python object.

    Returns:
    object: The Python data structure represented by the JSON string.
    """
    python_obj = json.loads(my_str)
    return python_obj
