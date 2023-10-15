#!/usr/bin/python3

"""Module containing test cases for the Base class"""

import unittest
import json
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


if __name__ == "__main__":
    unittest.main()
