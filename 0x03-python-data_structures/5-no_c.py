#!/usr/bin/python3
def no_c(my_string):
    ch = ['c', 'C']
    new_string = "".join(char for char in my_string if char not in ch)
    return new_string
