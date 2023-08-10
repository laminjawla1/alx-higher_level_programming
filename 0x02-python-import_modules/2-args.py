#!/usr/bin/python3

from sys import argv, exit


def main():
    _len = len(argv) - 1

    if _len == 0:
        print("0 arguments.")
    elif _len == 1:
        print("{} argument:".format(_len))
    else:
        print("{} arguments:".format(_len))
    for i, arg in enumerate(argv[1:], start=1):
        print("{}: {}".format(i, arg))


if __name__ == "__main__":
    main()
