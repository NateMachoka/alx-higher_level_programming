#!/usr/bin/python3

"""Module containing test cases for the Square class"""
from models.base import Base
from models.square import Square
import unittest
import io


class TestSquare(unittest.TestCase):
    def test_valid_constructor(self):
        # Test creating a valid Square instance
        s = Square(5, 3, 4, 1)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)  # Width and height should be equal
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_area(self):
        # Test calculating the area of a Square
        s = Square(4)
        self.assertEqual(s.area(), 16)  # 4 * 4 = 16

    def test_display(self):
        # Test the display method by capturing stdout
        s = Square(3)
        expected_output = "###\n###\n###\n"

        with unittest.mock.patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            s.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str(self):
        # Test the __str__ method
        s = Square(2, 1, 1, 10)
        expected_str = "[Square] (10) 1/1 - 2"
        self.assertEqual(str(s), expected_str)

if __name__ == "__main__":
    unittest.main()
