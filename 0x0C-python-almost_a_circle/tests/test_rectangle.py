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


class TestRectangle(unittest.TestCase):
    # ... (previous test cases)

    def test_display(self):
        # Test the display method by capturing stdout
        r = Rectangle(3, 2)
        expected_output = "###\n###\n"

        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
