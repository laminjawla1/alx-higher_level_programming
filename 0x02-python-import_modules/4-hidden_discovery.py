#!/usr/bin/python3.8

import hidden_4


def main():
    for name in dir(hidden_4):
        print(name) if not name.startswith("__") else print(end="")


if __name__ == "__main__":
    main()
