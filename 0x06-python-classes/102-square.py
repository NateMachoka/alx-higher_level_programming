#!/usr/bin/python3

"""Square class

This module contains a class called Square that represents a square.

"""


class Square:
    """A square shape class

    A basic class representing a square shape.

    Attributes:
        __size (float or int): size of the square.
    """

    def __init__(self, size=0):
        """Initialize a square instance with an optional size.

        Args:
            size (float or int, optional): The size of square.Default is 0.

        Raises:
            TypeError: If size is not a number (float or int).
            ValueError: If size is less than 0.
        """
        if not isinstance(size, (float, int)):
            raise TypeError("size must be a number")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """Get the size of the square.

        Returns:
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (float or int): The new size of the square.

        Raises:
            TypeError: If value is not a number (float or int).
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.__size * self.__size

    def __eq__(self, other):
        """Check if two squares have the same area.

        Args:
            other (Square): Another square to compare with.

        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares have different areas.

        Args:
            other (Square): Another square to compare with.

        Returns:
            bool: True if the areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if the area of the square is less than the area of another
        square.

        Args:
            other (Square): Another square to compare with.

        Returns:
            bool: True if the area is less, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """Check if the area of the square is less than or equal to the area of
        another square.

        Args:
            other (Square): Another square to compare with.

        Returns:
            bool: True if the area is less than or equal, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if the area of the square is greater than the area of another
        square.

        Args:
            other (Square): Another square to compare with.

        Returns:
            bool: True if the area is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if the area of the square is greater than or equal to the area
        of another square.

        Args:
            other (Square): Another square to compare with.

        Returns:
            bool: True if the area is greater than or equal, False otherwise.
        """
        return self.area() >= other.area()
