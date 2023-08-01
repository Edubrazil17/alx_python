#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []

#using for loop to iterate throght the matrix 
    for row in matrix:
        new_row = [x**2 for x in row]
        new_matrix.append(new_row)

#retuen the new value 
    return new_matrix
