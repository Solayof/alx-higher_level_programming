#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_dup = my_list.copy()
    if idx >= 0 and idx < len(my_list):
        list_dup[idx] = element
    return list_dup
