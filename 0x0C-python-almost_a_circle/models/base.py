#!/usr/bin/python3
"""bases for all the classes

"""


class Base():
    """
    delcare class Bases
    Class Attributes:
        __nb_objects
    Method:
        __init__(self, id=None)
    Class Methods:

    Class Methods:
    """
    __nb_objects = 0

    def __init__(self, id=0):
        """intializing id"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        