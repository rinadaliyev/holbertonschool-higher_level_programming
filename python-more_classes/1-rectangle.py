#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Rectangle class with width property."""

    def __init__(self, width=0):
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
