#!/usr/bin/python3

class Square:
    """
    The `Square` class represents a square shape with a private size attribute.

    Attributes:
        __size (int): The size (side length) of the square.

    Methods:
        __init__(self, size):
            Initializes a new square instance with the given size.

        area(self):
            Calculates and returns the area of the square.

    Usage:
        To create and use a `Square` object, first import the class into your
Python script.
        Then, create instances of the `Square` class and use its methods to
work with squares.
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
