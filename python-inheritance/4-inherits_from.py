#!/usr/bin/python3
"""test"""


def inherits_from(obj, a_class):
    """Test 12313131"""
    
    if issubclass(type(obj), a_class) and type(obj) != a_class:
       return True
       
    return False
