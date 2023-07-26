#!/usr/bin/python3

def convert_to_celsus(fahrenhelt):
    celsus = (fahrenhelt - 32)*5/9
    return celsus

print(convert_to_celsus(78))
print(convert_to_celsus(100))
print(convert_to_celsus(-40))
print(convert_to_celsus(-459.67))
