#!/usr/bin/python3
"""
module 2-is_same_class.py

contains methods that return true if the object is exactly an instance of 
the specified class ; otherwise False.

"""

def is_same_class(obj, a_class):
    """
    function that check if obj is instance of a_class

    Retrun:
        returns True if obj is exactly an isntance of a_class
    """

    return type(obj) == a_class
