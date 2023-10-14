#!/usr/bin/python3

"""Module containing test cases for the Rectangle class"""

import unittest
import io
from models.rectangle import Rectangle
from models.base import Base
from unittest.mock import patch


class TestRectangle(unittest.TestCase):
    def test_valid_constructor(self):
        # Test creating a valid Rectangle instance
        r = Rectangle(10, 20, 3, 4, 1)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_invalid_width(self):
        # Test creating a Rectangle with an invalid width
        with self.assertRaises(ValueError):
            Rectangle(0, 20, 3, 4, 1)

    def test_invalid_height(self):
        # Test creating a Rectangle with an invalid height
        with self.assertRaises(ValueError):
            Rectangle(10, -5, 3, 4, 1)

    def test_invalid_x(self):
        # Test creating a Rectangle with an invalid x-coordinate
        with self.assertRaises(ValueError):
            Rectangle(10, 20, -3, 4, 1)

    def test_invalid_y(self):
        # Test creating a Rectangle with an invalid y-coordinate
        with self.assertRaises(ValueError):
            Rectangle(10, 20, 3, -4, 1)

    def test_invalid_width_type(self):
        # Test creating a Rectangle with an invalid width type
        with self.assertRaises(TypeError):
            Rectangle("invalid", 20, 3, 4, 1)

    def test_invalid_height_type(self):
        # Test creating a Rectangle with an invalid height type
        with self.assertRaises(TypeError):
            Rectangle(10, None, 3, 4, 1)

    def test_invalid_x_type(self):
        # Test creating a Rectangle with an invalid x-coordinate type
        with self.assertRaises(TypeError):
            Rectangle(10, 20, "invalid", 4, 1)

    def test_invalid_y_type(self):
        # Test creating a Rectangle with an invalid y-coordinate type
        with self.assertRaises(TypeError):
            Rectangle(10, 20, 3, [4], 1)

    def test_area(self):
        # Test calculating the area of a Rectangle
        r = Rectangle(5, 4)
        self.assertEqual(r.area(), 20)

    def test_display(self):
        # Test the display method by capturing stdout
        r = Rectangle(3, 2)
        expected_output = "###\n###\n"

        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str(self):
        # Test the __str__ method
        r = Rectangle(3, 2, 1, 1, 10)
        expected_str = "[Rectangle] (10) 1/1 - 3/2"
        self.assertEqual(str(r), expected_str)

    def test_display_with_offset(self):
        # Test the display method with x and y offsets
        r = Rectangle(3, 2, 2, 1)
        expected_output = '\n  ###\n  ###\n'

        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_update_with_args(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(6, 7, 8, 9, 10)

        self.assertEqual(r.id, 6)
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 8)
        self.assertEqual(r.x, 9)
        self.assertEqual(r.y, 10)

    def test_update_with_subset_of_args(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(6, 7, 8)

        self.assertEqual(r.id, 6)
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 8)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_update_with_no_args(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update()

        self.assertEqual(r.id, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)


if __name__ == "__main__":
    unittest.main()
