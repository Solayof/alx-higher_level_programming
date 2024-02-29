#!/usr/bin/python3
"""Function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    low = 0
    high = len(list_of_integers) - 1

    while low <= high:
        mid = (low + high) // 2

        # Check if mid is a peak
        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1])\
                and (mid == len(list_of_integers) - 1
                     or list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]

        # Move towards the direction of the greater neighbor
        if mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return None
