#!/usr/bin/python3

from sys import argv, exit
from calculator_1 import (add, sub, mul, div)


def main():
	if len(argv) != 4:
		print("Usage: ./100-my_calculator.py <a> <operator> <b>")
		exit(1)
	calculate()
if __name__ == "__main__":
	main()
