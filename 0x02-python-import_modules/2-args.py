#!/usr/bin/python3

from sys import argv


def main():
    argv_len = len(argv) - 1

    if argv_len > 2:
        print("{} arguments:".format(argv_len))
    else:
        print("{} argument:".format(argv_len))
    for i, arg in enumerate(argv[1:], start=1):
        print("{}: {}".format(i, arg))


if __name__ == "__main__":
    main()
