#!/usr/bin/python3

"""Module containing test cases for the Base class"""

import unittest
import json
import os
from models.helpers import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

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

    def test_create_with_rectangle(self):
         # Import the Rectangle class here
        from models.rectangle import Rectangle

        # Create a dictionary with attributes for a Rectangle
        attrs = {'id': 1, 'width': 10, 'height': 4, 'x': 0, 'y': 0}

        # Create a Rectangle instance using the create method
        r = Rectangle.create(**attrs)

        # Check if the created instance is of type Rectangle
        self.assertIsInstance(r, Rectangle)

        # Check if the attributes match the expected values
        self.assertEqual(r.id, attrs['id'])
        self.assertEqual(r.width, attrs['width'])
        self.assertEqual(r.height, attrs['height'])
        self.assertEqual(r.x, attrs['x'])
        self.assertEqual(r.y, attrs['y'])

    def test_create_with_square(self):
        # Create a dictionary with attributes for a Square
        attrs = {'id': 1, 'size': 5, 'x': 2, 'y': 2}

        # Create a Square instance using the create method
        s = Square.create(**attrs)

        # Check if the created instance is of type Square
        self.assertIsInstance(s, Square)

        # Check if the attributes match the expected values
        self.assertEqual(s.id, attrs['id'])
        self.assertEqual(s.size, attrs['size'])
        self.assertEqual(s.x, attrs['x'])
        self.assertEqual(s.y, attrs['y'])

    def test_load_from_file_with_existing_file(self):
        # Create and save some instances to a JSON file
        r1 = Rectangle(10, 4)
        r2 = Rectangle(5, 5)
        r3 = Rectangle(7, 3)
        Rectangle.save_to_file([r1, r2, r3])

        # Load instances from the file
        instances = Rectangle.load_from_file()

        # Check if the instances are of the correct type
        self.assertIsInstance(instances, list)
        all_instances_are_rectangles = all(
            isinstance(instance, Rectangle) for instance in instances
            )
        self.assertTrue(all_instances_are_rectangles)

        # Check if the loaded instances match the ones saved
        self.assertEqual(len(instances), 3)
        self.assertEqual(instances[0].id, r1.id)
        self.assertEqual(instances[1].id, r2.id)
        self.assertEqual(instances[2].id, r3.id)

        # Clean up: remove the file
        os.remove("Rectangle.json")

    def test_load_from_file_with_non_existing_file(self):
        # Try to load from a non-existing file
        instances = Square.load_from_file()

        # Check if the result is an empty list
        self.assertEqual(instances, [])

    def setUp(self):
        # Initialize test objects
        self.rectangles = [Rectangle(1, 2, 3, 4, 5), Rectangle(6, 7, 8, 9, 10)]
        self.squares = [Square(11, 12, 13, 14), Square(15, 16, 17, 18)]

    def test_save_and_load_rectangle_csv(self):
        # Test saving and loading Rectangle objects to/from CSV
        Rectangle.save_to_file_csv(self.rectangles)
        loaded_rectangles = Rectangle.load_from_file_csv()

        self.assertEqual(len(loaded_rectangles), 2)
        self.assertEqual(loaded_rectangles[0].id, 5)
        self.assertEqual(loaded_rectangles[1].id, 10)

    def test_save_and_load_square_csv(self):
        # Test saving and loading Square objects to/from CSV
        Square.save_to_file_csv(self.squares)
        loaded_squares = Square.load_from_file_csv()

        self.assertEqual(len(loaded_squares), 2)
        self.assertEqual(loaded_squares[0].id, 14)
        self.assertEqual(loaded_squares[1].id, 18)

    def tearDown(self):
        # Clean up the CSV files after the tests
        if os.path.exists("Rectangle.csv"):
            os.remove("Rectangle.csv")
        if os.path.exists("Square.csv"):
            os.remove("Square.csv")


if __name__ == "__main__":
    unittest.main()
