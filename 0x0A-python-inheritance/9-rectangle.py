#!/usr/bin/python3

"""Module containing a class Rectangle that inherits from BaseGeometry.
"""


class BaseGeometry:
    """A class representing a basic geometry object.
    """

    def area(self):
        """Calculate the area of the geometry object.

        Raises:
            Exception: This method is not implemented in the base class.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate an integer value for a given attribute.

        Args:
            name (str): The name of the attribute being validated
(always a string).
            value (int): The value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """A class representing a rectangle.

    Attributes:
        __width (int): The width of the rectangle (positive integer).
        __height (int): The height of the rectangle (positive integer).
    """

    def __init__(self, width, height):
        """Initialize a rectangle with a given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the rectangle.

        Returns:
            str: A string describing the rectangle in the format [Rectangle]
<width>/<height>.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
