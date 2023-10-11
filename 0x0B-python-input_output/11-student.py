#!/usr/bin/python3

"""Module for defining the Student class"""


class Student:
    """
    Class to represent a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance with first name, last name, and age.

        Parameters:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.

        Parameters:
            attrs (list, optional): list of strings specifying attribute names
                If None, retrieve all attributes.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__

        json_data = {}
        for attr in attrs:
            if hasattr(self, attr):
                json_data[attr] = getattr(self, attr)
        return json_data

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance using a dictionary.

        Parameters:
            json (dict): dictionary with attribute names and their values
        """
        for key, value in json.items():
            setattr(self, key, value)
