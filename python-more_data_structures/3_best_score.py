#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or not a_dictionary:
        return None

# initialize varibles to track of the highest value and corresponding key

    best_score = float('-inf')# start with negative inifinity
    best_key = None

# iterate through the a_dictionary for the best_score and corresponding key

    for key, value in a_dictionary.items():

# check if value is greater than current value 
        if value > best_score:

#if it does, update best_score and it corresponding key 
           best_score = value
           best_key = key

    return best_key
