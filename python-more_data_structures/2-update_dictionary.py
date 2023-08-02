#1/usr/bin/python3

def update_dictionary(a_dictionary, key, value):

# check if key is in dictionary
    if key in a_dictionary:
        a_dictionary[key] = value

# if not add new key value pair
    else:
        a_dictionary[key] = value

    return a_dictionary
