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

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size attribute.

        Args:
            value (int): Size of the square.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args:
            attrs = ["id", "size", "x", "y"]
            for i in range(len(args)):
                if i < len(attrs):
                    setattr(self, attrs[i], args[i])
            return  # Return early to avoid conflicting updates

        for key, value in kwargs.items():
            if key == "size":
                self.width = value  # Update width
                self.height = value  # Update height
            elif hasattr(self, key):
                setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary representation of the Square."""
        square_dict = {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
        return square_dict
