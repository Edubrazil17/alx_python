#!/usr/bin/python3

def is_prime(number):

    if number <= 1:
     return false

    elif number <= 3:
     return true

    elif number % 2 == 0 or number % 3 == 0:
     return false

 i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6

    return True
