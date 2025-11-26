#!/usr/bin/python3
"""Hzynn"""


def inherits_from(obj, a_class):
    """loremimpus"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
       return True
    return False
