#!/usr/bin/python3

import sys

def print_argument():
    num_arg = len(sys.argv)-1

    if num_arg == 0:
        print("0 arguments:")
    elif num_arg == 1:
        print("1 argument:")
    else:
        print(f"{num_arg}" " arguments:")

    if num_arg > 0:
        for i in range(1, num_arg + 1 ):
            print(f"{i}:{sys.argv[i]}")

            
if __name__ == "__main__":
   print_argument()
