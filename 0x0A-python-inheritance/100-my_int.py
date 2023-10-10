#!/usr/bin/python3

"""Module containing a class MyInt that inherits from int.
"""


class MyInt(int):
    """A class representing a rebellious integer.

    Inherits from int, but inverts the == and != operators.
    """

    def __eq__(self, other):
        """Override the equality operator (==) to invert it.

        Args:
            other (int): The integer to compare with.

        Returns:
            bool: True if self is not equal to other, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the inequality operator (!=) to invert it.

        Args:
            other (int): The integer to compare with.

        Returns:
            bool: True if self is equal to other, False otherwise.
        """
        return super().__eq__(other)
