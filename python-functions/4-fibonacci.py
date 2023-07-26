#!/usr/bin/python3

def fibonacci_sequence(n):
    fibonacci_sequence = [0, 1]
    
    #while loop code for the sequenc

    while len(fibonacci_sequence) < n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence[:n]

#call the function to print the fib. sequence of given numbr
n = 8
print(fibonacci_sequence(8))

n = 10
print(fibonacci_sequence(10))

n = 50
print(fibonacci_sequence(50))

n = 1
print(fibonacci_sequence(1))
