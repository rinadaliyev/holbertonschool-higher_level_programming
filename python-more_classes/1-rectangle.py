#!/usr/bin/python3
"""Defines an empty Rectangle class."""

class Rectangle:
"""Rectangle comment"""
	@property
	def width(self):
		return self.__width
	@width.setter
	def __width(self, value):
        self.__width = value
