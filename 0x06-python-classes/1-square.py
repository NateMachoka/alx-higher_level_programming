#!/usr/bin/python3


"""Has a square class
This module contains a simple square class called Square.
"""


class Square:
    """A square shape class

    A basic class representing a square shape.

    Attributes:
        None
    """
    def __init__(self, size):
        """
        Initializes a new square instance with the given size.

        Args:
            size (int): The size (side length) of the square.
        """
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
