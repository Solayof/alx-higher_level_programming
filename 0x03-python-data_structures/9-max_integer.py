#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        ma = my_list[0]
        for i in my_list:
            if i > ma:
                ma = i
        return ma
    else:
        return None
