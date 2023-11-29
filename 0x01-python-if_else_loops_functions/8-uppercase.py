#!/usr/bin/python3
def uppercase(str):
    str = ord(str)
    for str in range(65, 123):
        if str >= 97:
            str = str - 32
            return(chr(str))
        else:
            return(chr(str)
