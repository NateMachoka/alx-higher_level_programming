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
