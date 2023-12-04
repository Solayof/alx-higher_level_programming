#!/usr/bin/python3
""" MyList that inherit from list
"""


class MyList(list):
    """Inherits from list"""
    def print_sorted(self):
        """Prints list in ascending order"""
        print(sorted(self))
