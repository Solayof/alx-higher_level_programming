#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        val = []
        for i in my_list:
            if i % 2 == 0:
                val += [True]
            else:
                val += [False]
        return val
