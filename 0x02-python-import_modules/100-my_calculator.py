#!/usr/bin/python3

from sys import argv, exit
from calculator_1 import add, sub, mul, div


def main():
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    calculate(argv[1], argv[2], argv[3])


def calculate(n1, op, n2):
    n1 = int(n1)
    n2 = int(n2)
    match (op):
        case "+":
            print("{} + {} = {}".format(n1, n2, add(n1, n2)))
        case "-":
            print("{} - {} = {}".format(n1, n2, sub(n1, n2)))
        case "*":
            print("{} * {} = {}".format(n1, n2, mul(n1, n2)))
        case "/":
            print("{} / {} = {}".format(n1, n2, div(n1, n2)))
        case _:
            print("Unknown operator. Available operators: +, -, * and /")


if __name__ == "__main__":
    main()
