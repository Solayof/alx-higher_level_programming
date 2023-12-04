#!/usr/bin/python3
"""
module 1-my_list.py
contains a class Mylist that inherit list

"""


class Mylist(list):
    """inherits from list

    method:
    print_sorted(self)

    """
    def print_sorted(self):
        """print the list sorted in ascending order"""

        print(sorted(self))
