#!/usr/bin/python3

"""Module containing test cases for the Square class"""
from models.base import Base
from models.square import Square
import unittest
from unittest.mock import patch
import io


class TestSquare(unittest.TestCase):
    def test_valid_constructor(self):
        # Test creating a valid Square instance
        s = Square(5, 3, 4, 1)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_size_getter(self):
        # Test the size getter
        s = Square(3, 0, 0)
        self.assertEqual(s.size, 3)

    def test_size_setter(self):
        # Test the size setter
        s = Square(3, 0, 0)
        s.size = 7
        self.assertEqual(s.size, 7)
        self.assertEqual(s.width, 7)
        self.assertEqual(s.height, 7)

    def test_size_invalid_value(self):
        # Test setting an invalid size
        s = Square(3, 0, 0)
        with self.assertRaises(ValueError):
            s.size = -2

    def test_size_invalid_type(self):
        # Test setting an invalid size type
        s = Square(3, 0, 0)
        with self.assertRaises(TypeError):
            s.size = "invalid"

    def test_update_with_args(self):
        # Test updating with *args
        s = Square(1, 2, 3, 4)
        s.update(6, 7)

        self.assertEqual(s.id, 6)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 2)  # x should not change
        self.assertEqual(s.y, 3)  # y should not change

    def test_update_with_kwargs(self):
        # Test updating with **kwargs
        s = Square(1, 2, 3, 4)
        s.update(size=7, x=8)

        self.assertEqual(s.id, 4)  # ID should not change
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 8)
        self.assertEqual(s.y, 3)  # Y should not change

    def test_update_with_subset_of_args(self):
        # Test updating with a subset of *args
        s = Square(1, 2, 3, 4)
        s.update(6, 7, x=8)

        self.assertEqual(s.id, 6)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)  # y should not change

    def test_update_with_both(self):
        # Test updating with both *args and **kwargs
        s = Square(1, 2, 3, 4)
        s.update(6, size=7, x=8, y=9)

        self.assertEqual(s.id, 6)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)


if __name__ == "__main__":
    unittest.main()
