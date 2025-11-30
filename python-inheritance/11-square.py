#!/usr/bin/python3
"""
11-square: Defines a Square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square.
    """

    def __init__(self, size):
        """
        Initialize a new Square.

        Args:
            size (int): Length of each side.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Returns the area of the Square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns the string representation of the Square.
        """
        return "[Square] {}/{}".format(
            self.__size, self.__size
        )
