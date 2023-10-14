#!/usr/bin/python3

"""A module that has a Base class"""


class Base:
    """Base class for managing id attribute in other classes."""

    # Private class attribute to keep track of the number of objects created
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor to initialize id attribute.

        Args:
            id (int): An optional integer representing the object's ID.

        Attributes:
            id (int): A public instance attribute representing the object's ID.
        """
        if id is not None:
            if not isinstance(id, int):
                raise TypeError("id must be an integer")
            if id <= 0:
                raise ValueError("id must be > 0")
            self.id = id
        else:
            # If id isn't provided, increment __nb_objects;assign the new value
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
