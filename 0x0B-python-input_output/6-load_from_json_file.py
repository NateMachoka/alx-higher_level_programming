#!/usr/bin/python3

"""Module for loading an object from a JSON file"""

import json


def load_from_json_file(filename):
    """
    Create a Python object from a JSON file.

    Parameters:
    filename (str): The name of the JSON file to load the object from.

    Returns:
    object: The Python object loaded from the JSON file.
    """
    # Open the file in read mode using the with statement
    with open(filename, 'r') as file:
        # Load the JSON data from the file and parse it into a Python object
        data = json.load(file)

    return data
