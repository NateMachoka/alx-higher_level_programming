#!/usr/bin/python3

"""Module containing a class BaseGeometry.
"""


class BaseGeometry:
    """A class representing a basic geometry object.
    """

    def area(self):
        """Calculate the area of the geometry object.

        Raises:
            Exception: This method is not implemented in the base class.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate an integer value for a given attribute.

        Args:
            name (str): The name of the attribute being validated
       (always a string).
            value (int): The value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
