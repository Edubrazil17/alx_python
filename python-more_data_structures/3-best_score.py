#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or not a_dictionary:
        return None
# initialize variable to track the hishest score
    max_score = None
    best_key = None

    #iterate through the dictionary 

    for key, value in a_dictionary.items():

        #check if value is greater than the current value
        if max_score is None or value > max_score:

            #if it does, update max_score
            max_score = value
            best_key = key

    return best_key
