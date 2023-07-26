#!/usr/bin/python3

def fibonacci_sequence(n):
    fibonacci_sequence = [0, 1]
    
    #while loop code for the sequenc

    while len(fibonacci_sequence) < n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence[:n]
