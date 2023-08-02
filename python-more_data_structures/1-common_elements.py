#!/usr/bin/python3

def common_elements(set_1, set_2):
# initialise an empty set to store the common element
    common_set = set()

# use for loop to iterate the first set
    for element in set_1:

# check if element is present in second set 
        if element in set_2:

# if it does add the common element 
            common_set.add(element)

    return common_set
