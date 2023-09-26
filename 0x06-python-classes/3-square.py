#!/usr/bin/python3

""" Square Class

This module contains a Square class that represents a square shape.

"""

class Square:
    """Square shape class

    This class represents a square shape with a private size attribute and
    a method to calculate its area.

    Attributes:
        __size (int): The size (side length) of the square.
    """

    def __init__(self, size=0):
        """Initialize a new square instance with an optional size.

        Args:
            size (int, optional): The size (side length) of the square.
                Default is 0.

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
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
