#!/usr/bin/python3

def validate_password(password):
    #check for lenght of the password

    if len(password) < 8:
        return false

    #check for uppercase, lowercase and digit

    has_uppercase = false 
    has_lowercase = false
    has_digit = false 

    for char in password:
        if char.isupper():
            has_uppercase = true

        elif char.islower():
            has_lowercase = true

        elif char.isdigit():
            has_digit = true

    if not(has_uppercase and has_lowercase and has_digit):
        return false

    #check for spaces

    if " " in password:
        return false

    return true 

