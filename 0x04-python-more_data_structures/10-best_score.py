#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maxval = 0
    maxkey = None
    for k, i in a_dictionary.items():
        if i > maxval:
            maxval = i
            maxval = k
    return maxkey
