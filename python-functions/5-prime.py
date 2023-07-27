#!/usr/bin/python3

def is_prime(number):

    #This is the first condition that checks if the number is less than 2. Since prime numbers are greater than 1
    if number < 2:
        return false

#This is a loop that iterates from 2 to the square root of the input number (inclusive)
    for i in range (2, int(number **0.5) + 1):

        if number % i == 0:
            return false

        return true
