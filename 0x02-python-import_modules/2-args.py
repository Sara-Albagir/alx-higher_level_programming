#!/usr/bin/python3
arg = input("Enter sth: ")
arg = arg.split()
count = len(arg)
if count == 0:
    print("0 arguments")
elif count == 1:
    print("{} argument:".format(count))
    print("1: {}".format(arg[0]))
else:
    print("{} arguments:".format(count))
    for i in range(count):
        print("{}: {}".format(i + 1, arg[i]))
