#!/usr/bin/python3

class Square:
    """
    This class defines a square with a private size attribute.
    """

    def __init__(self, size):
        """
        Initializes a new square instance with the given size.
        :param size: The size of the square.
        """
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.
        :return: The area of the square.
        """
        return self.__size * self.__size
