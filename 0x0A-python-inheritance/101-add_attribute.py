#!/usr/bin/python3

"""Module containing a function to add a new attribute to an object.
"""

def add_attribute(obj, attr_name, attr_value):
    """Add a new attribute to an object if possible.

    Args:
        obj (object): The object to which the attribute should be added.
        attr_name (str): The name of the attribute to be added.
        attr_value: The value of the attribute to be added.

    Raises:
        TypeError: If the object cannot have new attributes.
    """
    if hasattr(obj, '__dict__') or (hasattr(type(obj), '__slots__')
                                    and attr_name in type(obj).__slots__):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
