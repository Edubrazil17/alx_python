#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or not a_dictionary:
        return None
# initialize two vavriables to keep track of maximum number and key found in the dictionary

    max_value = None
    best_key = None

# iterate through the a_dictionary key/value pair

    for key, value in a_dictionary.items():

#check if max_value is none or current value is greater than max_value
        if max_value is None or value > max_value:
#if either of this condition is true update the max_value and best_key
            max_value = value
            best_key = key

    return best_key
