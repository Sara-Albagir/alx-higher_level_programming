#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    count = len(calculator_1.argv)
    if count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b> ")
        sys.exit(1)
    for i in range(count):
        if calculator_1.argv[1] != '+' or calculator_1.argv[1] != '-' or calculator_1.argv[1] != '*' or calculator_1.argv[1] != '/':
            print("Unknown operator. Available operators: +, -, * and / ")
            sys.exit(1)

