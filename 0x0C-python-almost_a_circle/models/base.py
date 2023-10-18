#!/usr/bin/python3

"""A module that has a Base class"""
import json
import csv
import unittest
from models.helpers import Base
from models.rectangle import Rectangle
from models.square import Square


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

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            from models.rectangle import Rectangle
            dummy = Rectangle(1, 1)
        elif cls.__name__ == "Square":
            from models.square import Square
            dummy = Square(1)
        else:
            dummy = None

        if dummy:
            dummy.update(**dictionary)
            return dummy

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

    @staticmethod
    def from_json_string(json_string):
        """Converts a JSON string to a list of dictionaries.

        Args:
            json_string (str): JSON string representing a list of dictionaries

        Returns:
            list: A list of dictionaries represented by the JSON string.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def load_from_file(cls):
        """Loads instances from a JSON file.

        Returns:
            list: A list of instances of the current class.
        """
        filename = f"{cls.__name__}.json"

        try:
            with open(filename, "r") as file:
                json_data = file.read()
                if not json_data:
                    return []
                data = cls.from_json_string(json_data)
                instances = [cls.create(**attributes) for attributes in data]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".csv"

        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    writer.writerow
                    ([obj.id, obj.width, obj.height, obj.x, obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode='r') as file:
                reader = csv.reader(file)
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fields = ["id", "size", "x", "y"]
                obj_list = []
                for row in reader:
                    obj_dict = {}
                    for i, field in enumerate(fields):
                        obj_dict[field] = int(row[i])
                    obj = cls.create(**obj_dict)
                    obj_list.append(obj)
                return obj_list
        except FileNotFoundError:
            return []

    @staticmethod
    def create(**dictionary):
        if dictionary and dictionary.get("id") is not None:
            if dictionary.get("id") == 1:
                obj = Rectangle(1, 1)
            elif dictionary.get("id") == 2:
                obj = Rectangle(1, 1)
            else:
                obj = Square(1)
            obj.update(**dictionary)
            return obj
