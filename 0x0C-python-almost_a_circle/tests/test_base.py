#!/usr/bin/python3

"""Module containing test cases for the Base class"""

import unittest
import json
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    def test_id_generation(self):
        # Test the automatic ID generation
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)  # first instance should have ID of 1
        self.assertEqual(base2.id, 2)  # second instance should have ID of 2

    def test_custom_id(self):
        # Test creating an instance with a custom ID
        base = Base(100)
        self.assertEqual(base.id, 100)  # The ID should be set to 100

    def test_invalid_custom_id(self):
        # Test creating an instance with an invalid custom ID
        with self.assertRaises(ValueError):
            Base(0)  # Should raise a ValueError because ID must be > 0

    def test_invalid_custom_id_type(self):
        # Test creating an instance with an invalid custom ID type
        with self.assertRaises(TypeError):
            Base("not_an_integer")  # Should raise a TypeError

    def test_to_json_string_empty(self):
        """Test to_json_string with an empty list."""
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_to_json_string_none(self):
        """Test to_json_string with a None list."""
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_string_with_data(self):
        """Test to_json_string with a list of dictionaries."""
        data = [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"},
            {"id": 3, "name": "Charlie"}
        ]
        json_string = Base.to_json_string(data)
        part1 = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}, '
        part2 = '{"id": 3, "name": "Charlie"}]'
        expected_json = part1 + part2
        self.assertEqual(json_string, expected_json)

    def test_save_to_file_with_rectangles(self):
        # Create a list of Rectangle objects
        r1 = Rectangle(10, 4)
        r2 = Rectangle(5, 5)
        r3 = Rectangle(7, 3)
        list_rectangles = [r1, r2, r3]
        # Save the list to a file
        Rectangle.save_to_file(list_rectangles)

        # Check if the file exists
        self.assertTrue(os.path.exists("Rectangle.json"))

        # Read the contents of the file
        with open("Rectangle.json", "r") as file:
            contents = file.read()

        # Sort the list of dictionaries by ID for comparison
        sorted_list = sorted(list_rectangles, key=lambda x: x.id)
        expected_json = json.dumps([obj.to_dictionary
                                    () for obj in sorted_list])

        # Compare the JSON strings
        self.assertEqual(contents, expected_json)

        # Clean up: remove the file
        os.remove("Rectangle.json")

    def test_save_to_file_with_squares(self):
        # Create a list of Square objects
        s1 = Square(4)
        s2 = Square(7)
        s3 = Square(2)
        list_squares = [s1, s2, s3]
        # Save the list to a file
        Square.save_to_file(list_squares)

        # Check if the file exists
        self.assertTrue(os.path.exists("Square.json"))

        # Read the contents of the file
        with open("Square.json", "r") as file:
            contents = file.read()

        # Sort the list of dictionaries by ID for comparison
        sorted_list = sorted(list_squares, key=lambda x: x.id)
        expected_json = json.dumps([obj.to_dictionary
                                    () for obj in sorted_list])

        # Compare the JSON strings
        self.assertEqual(contents, expected_json)

        # Clean up: remove the file
        os.remove("Square.json")

    def test_from_json_string_with_valid_json(self):
        json_string = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        expected_list = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]

        result = Base.from_json_string(json_string)

        self.assertEqual(result, expected_list)

    def test_from_json_string_with_empty_json(self):
        json_string = ''
        expected_list = []

        result = Base.from_json_string(json_string)

        self.assertEqual(result, expected_list)

    def test_from_json_string_with_none(self):
        json_string = None
        expected_list = []

        result = Base.from_json_string(json_string)

        self.assertEqual(result, expected_list)


if __name__ == "__main__":
    unittest.main()
