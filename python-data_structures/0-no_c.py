#!/usr/bin/python3

def no_c(my_string):
    
    new_string = ""

#using for loop to search for character "c, C" in string
for char in my_string:
    if char not in ("c","C"):
        new_string += char

return new_string
