#!/usr/bin/python3

"""Module for the Square class"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor to initialize a Square object.

        Args:
            size (int): Size of the square.
            x (int): X-coordinate of the square's position.
            y (int): Y-coordinate of the square's position.
            id (int): An optional ID for the square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Override the string representation of the Square.

        Returns:
            str: A formatted string representing the Square.
        """
        return (
            f"[Square] ({self.id}) "
            f"{self.x}/{self.y} - {self.width}"
        )
