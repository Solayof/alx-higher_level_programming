#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary:
        dic2 = {key: value}
        a_dictionary.update(dic2)
        return(a_dictionary)
    else:
        return None
