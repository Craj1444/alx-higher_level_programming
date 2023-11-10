#!/usr/bin/python3
def weight_average(my_list=[]):
    """
    A function that returns the weighted average of all integers tuple (<score>, <weight>)
    """
    if not my_list:
        return 0
    scores, weights = zip(*my_list)
    return sum(map(lambda x, y: x * y, scores, weights)) / sum(weights)
