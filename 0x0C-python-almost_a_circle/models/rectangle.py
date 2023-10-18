#!/usr/bin/python3


"""A module that has a Rectangle class"""
from models.base import Base
from models.rectangle import Rectangle


class Rectangle(Base):
    """Rectangle class that inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor to initialize a Rectangle object.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): X-coordinate of the rectangle's position.
            y (int): Y-coordinate of the rectangle's position.
            id (int): An optional ID for the rectangle.

        Attributes:
            id (int): Public instance attribute representing the object's ID.
            width (int): Private instance attribute for the rectangle's width.
            height (int): Private instance attribute for rectangle's height
            x (int): Private instance attribute for the X-coordinate.
            y (int): Private instance attribute for the Y-coordinate.
        """
        # Call the constructor of the base class with the provided ID
        super().__init__(id)

        # Set private attributes using setter methods
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter method for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width.

        Args:
            value (int): Width value to set.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height.

        Args:
            value (int): Height value to set.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter method for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x.

        Args:
            value (int): X-coordinate value to set.

        Raises:
            TypeError: If x is not an integer.
            ValueError: If x is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter method for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for y.

        Args:
            value (int): Y-coordinate value to set.

        Raises:
            TypeError: If y is not an integer.
            ValueError: If y is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """Print the rectangle using '#' characters to stdout."""
        for i in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        """Override the string representation of the Rectangle.

        Returns:
            str: A formatted string representing the Rectangle.
        """
        return (
            f"[Rectangle] ({self.id}) "
            f"{self.x}/{self.y} - {self.width}/{self.height}"
        )

    def display(self):
        """Print rectangle with '#' characters, considering x and y."""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def update(self, *args, **kwargs):
        """Update the attributes of the Rectangle using *args or **kwargs."""
        attrs = ["id", "width", "height", "x", "y"]

        if args:
            for i in range(len(args)):
                if i < len(attrs):
                    setattr(self, attrs[i], args[i])

        for key, value in kwargs.items():
            if key in attrs:
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the rectangle.

        Returns:
            dict: A dictionary containing id, width, height, x, and y.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def to_dictionary(self):
        """Returns the dictionary representation of the square.

        Returns:
            dict: A dictionary containing id, size, x, and y.
        """
        return {
            'id': self.id,
            'size': self.width,  # Width and size are the same for a square
            'x': self.x,
            'y': self.y
        }

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle instance."""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
