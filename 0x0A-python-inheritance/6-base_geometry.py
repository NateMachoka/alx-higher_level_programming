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
