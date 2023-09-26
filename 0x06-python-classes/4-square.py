#!/usr/bin/python3

""" Square Class

This module contains a Square class that represents a square shape.

"""


class Square:
    """Square shape class

    This class represents a square shape with a private size attribute,
    and methods to get and set its size, as well as calculate its area.

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
        self.__size = size

    @property
    def size(self):
        """Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size (side length) of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
