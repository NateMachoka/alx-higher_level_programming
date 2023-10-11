#!/usr/bin/python3

"""Module for converting an object to a JSON-serializable dictionary"""


def class_to_json(obj):
    """
    Convert an object to a dictionary description for JSON serialization.

    Parameters:
    obj (object): The object to be converted to a JSON-serializable dictionary.

    Returns:
    dict: dictionary representation of the object with serializable attributes
    """
    if not hasattr(obj, '__dict__'):
        raise ValueError("Input is not an instance of a class.")

    # Initialize an empty dictionary to store the serializable attributes
    json_dict = {}

    # Loop through the object's attributes
    for attr, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            # Add the attribute and its value to the dictionary
            json_dict[attr] = value

    return json_dict
