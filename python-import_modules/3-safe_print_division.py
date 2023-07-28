#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b

    #return none for division by 0
    except ZeroDivisionError:
        result = None

    #when all input is correct print result
    finally:
        print("inside result = {}".format(result))
        return result
        


a = 6
b= 3
result = safe_print_division(a, b)

print("{:d}/{:d} = {}".format(a, b,result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d}/{:d} = {}".format(a, b, result))
