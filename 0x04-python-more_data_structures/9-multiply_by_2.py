#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """
    A function that returns a new dictionary with all values multiplied by 2
    """
    new_dict = {}
    for key in a_dictionary:
        new_dict[key] = a_dictionary[key] * 2
    return new_dict
