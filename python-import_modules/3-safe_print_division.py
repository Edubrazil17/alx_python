#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b

    #return none for division by 0
    except ZeroDivisionError:
        result = None

    #when all input is correct print result
    finally:
        print("inside result: = {}".format(result))
        return result
