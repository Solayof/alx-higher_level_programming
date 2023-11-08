#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary:
        dict = {}
        tmp = {}
        for key, value in a_dictionary.items():
            val = value * 2
            tmp = {key: val}
            dict.update(tmp)
        return (dict)
    return None
