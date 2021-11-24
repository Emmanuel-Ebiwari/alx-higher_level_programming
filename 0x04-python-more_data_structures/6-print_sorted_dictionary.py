#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a_dict_items = a_dictionary.items()
    for key, value in sorted(a_dict_items, key=lambda d_items: d_items[0]):
        print("{}: {}".format(key, value))
