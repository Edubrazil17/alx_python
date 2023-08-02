#!/usr/bin/python3

def best_score(a_dictionary):

    if a_dictionary is None or not a_dictionary:
        return None

# initialize variable to keep track of best score and corresponding key
    best_score = float('-inf') #start with negative infinity
    best_key = None

# loop through the dictionary

    for key, value in a_dictionary.items():

#check if value is greater than the current value
        if value > best_score:

# if it does, update the best score and corresponding key
           best_score = value
           best_key = key

    return best_key
