#!/usr/bin/python3

"""A module that has a Base class"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: A JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.

        Args:
            cls: The class.
            list_objs (list): A list of instances inheriting from Base.

        Note:
            The filename will be based on the class name, e.g., Rectangle.json.
        """
        if list_objs is None:
            list_objs = []

        filename = f"{cls.__name__}.json"

        # Convert instances to dictionary representations
        dict_list = [obj.to_dictionary() for obj in list_objs]

        # Convert the dictionary list to a JSON string
        json_str = cls.to_json_string(dict_list)

        # Write the JSON string to the file, overwriting it if it exists
        with open(filename, "w") as file:
            file.write(json_str)
