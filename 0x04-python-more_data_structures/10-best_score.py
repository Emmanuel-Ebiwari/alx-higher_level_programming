#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    first_key = list(a_dictionary.keys())[0]
    max_val = a_dictionary[first_key]
    for key, val in a_dictionary.items():
        if val > max_val:
            ret = key
    return ret
