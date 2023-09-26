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

    def __init__(self, size=0):
        """Initializes a new square instance with an optional size.

        Args:
            size (int, optional): The size (side length) of the square. Default is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
