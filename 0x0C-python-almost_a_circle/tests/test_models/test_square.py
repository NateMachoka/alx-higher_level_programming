#!/usr/bin/python3

"""Module containing test cases for the Square class"""
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest


class TestSquare(unittest.TestCase):
    def test_constructor(self):
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertEqual(s.id, 1)  # Assuming no other squares created

    def test_str(self):
        s = Square(3, 1, 2, 4)
        expected_str = "[Square] (4) 1/2 - 3"
        self.assertEqual(str(s), expected_str)

    def test_size_property(self):
        s = Square(4)
        s.size = 7
        self.assertEqual(s.size, 7)
        self.assertEqual(s.width, 7)
        self.assertEqual(s.height, 7)

    def test_update(self):
        s = Square(5)
        s.update(10, 2, 3, 4)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_update_kwargs(self):
        s = Square(5)
        s.update(id=10, x=2, y=3, size=4)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 4)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_to_dictionary(self):
        s = Square(5, 1, 2, 4)
        expected_dict = {"id": 4, "size": 5, "x": 1, "y": 2}
        self.assertEqual(s.to_dictionary(), expected_dict)


if __name__ == "__main__":
    unittest.main()
