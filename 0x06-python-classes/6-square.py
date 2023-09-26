#!/usr/bin/python3

""" Square Class

This module contains a Square class that represents a square shape.

"""


class Square:
    """Square shape class

    This class represents a square shape with private size and position
    attributes, and methods to get and set them, as well as calculate its area
    and print a representation of the square.
    Attributes:
        __size (int): The size (side length) of the square.
        __position (tuple): The position of the square's top-left corner as
    (x, y) coordinates.

    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square instance with optional size and position.

        Args:
            size (int, optional): The size (side length) of the square.
        Default is 0.
            position (tuple, optional): The position of the square's top-left
        corner as (x, y) coordinates. Default is (0, 0).

        Raises:
            TypeError: If size is not an integer or position is not a tuple of
        2 positive integers.
            ValueError: If size is less than 0 or position contains non-positive
        integers.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif not isinstance(position, tuple) or len(position) != 2 or \
             not all(isinstance(coord, int) for coord in position) or \
             not all(coord >= 0 for coord in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__size = size
            self.__position = position

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

    @property
    def position(self):
        """Get the position of the square's top-left corner.

        Returns:
            tuple: The position as (x, y) coordinates.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square's top-left corner.

        Args:
            value (tuple): The new position as (x, y) coordinates.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
             not all(isinstance(coord, int) for coord in value) or \
             not all(coord >= 0 for coord in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """Print a representation of the square using '#' characters and
        respecting the position.

        If the size is 0, it prints an empty line.

        Returns:
            None
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
