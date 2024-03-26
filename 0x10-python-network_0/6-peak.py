#!/usr/bin/python3
"""
Function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    finds num that's greater than both left and right
    """
    if len(list_of_integers) == 0:
        return None

    list_int = list_of_integers
    beg = 0
    end = len(list_int)-1

    if list_int[beg] > list_int[beg+1]:
        return list_int[beg]
    if list_int[end] > list_int[end-1]:
        return list_int[end]

    mid = (beg+end)//2
    if list_int[mid-1] < list_int[mid] and list_int[mid+1] < list_int[mid]:
        return list_int[mid]
    if list_int[mid] < list_int[mid-1]:
        return find_peak(list_int[beg:mid+1])
    elif list_int[mid] < list_int[mid+1]:
        return find_peak(list_int[mid:end+1])
    else:
        return list_int[beg]
