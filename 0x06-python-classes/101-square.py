#!/usr/bin/python3

"""Square class

This module contains a class called Square that represents a square.

"""


class Square:
    """A square shape class

    A basic class representing a square shape.

    Attributes:
        __size (int): size of the square.
        __position (tuple): position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square instance with an optional size and position.

        Args:
            size (int, optional): The size (side length) of the square. Default
        is 0.
            position (tuple, optional): The position of the square. Default is
        (0, 0).

        Raises:
            TypeError: If size is not an integer or position is not a tuple of
        two positive integers.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif not isinstance(position, tuple) or len(position) != 2 or \
                not all(isinstance(i, int) for i in position) or \
                not all(i >= 0 for i in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__size = size
            self.__position = position

    @property
    def size(self):
        """Get the size (side length) of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size (side length) of the square.

        Args:
            value (int): The new size of the square.

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
        """Get the position of the square.

        Returns:
            tuple: The position of the square as atuple of two positive integer
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The new position of the square as a tuple of two
        positive integers.

        Raises:
            TypeError: If value is not a tuple of two positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) for i in value) or \
                not all(i >= 0 for i in value):
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
        """Print square using the character '#' with respect to its position

        If size is 0, print an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Represent the square as a string for printing.

        Returns:
            str: A string representation of the square.
        """
        square_str = ""
        if self.__size == 0:
            return square_str
        else:
            for i in range(self.__position[1]):
                square_str += "\n"
            for i in range(self.__size):
                square_str += " " * self.__position[0] + "#" * self.__size
                if i < self.__size - 1:
                    square_str += "\n"
            return square_str
