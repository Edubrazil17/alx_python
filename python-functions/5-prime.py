#!/usr/bin/python3

def is_prime(number):

    if number <= 1:
     return false

    elif number <= 3:
     return true

    elif number % 2 == 0 or number % 3 == 0:
     return false


