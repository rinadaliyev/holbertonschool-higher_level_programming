#!/usr/bin/python3
"""
8-rectangle module: Defines a Rectangle class that inherits from BaseGeometry.
"""

from 7-base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height
