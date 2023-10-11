#!/usr/bin/python3

"""Module for saving an object to a text file using JSON representation"""

import json


def save_to_json_file(my_obj, filename):
    """
    Write a Python object to a text file using its JSON representation.

    Parameters:
    my_obj (object): The object to be saved to the file.
    filename (str): The name of the file to save the JSON representation to.

    Returns:
    None
    """
    # Serialize the object to a JSON string
    json_string = json.dumps(my_obj)

    # Open the file in write mode using the with statement
    with open(filename, 'w') as file:
        # Write the JSON string to the file
        file.write(json_string)
