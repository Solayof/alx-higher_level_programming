#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        val = []
        for i in my_list:
            if i % 2 is 0:
                val.append(True)
            else:
                val.append(False)
        return val
