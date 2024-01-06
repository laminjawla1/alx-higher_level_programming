#!/usr/bin/python3
"""
Write a Python script that takes in a URL,
sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""
import sys
import requests


def main():
    response = requests.get(sys.argv[1])
    print(response.headers.get("X-Request-Id"))


if __name__ == "__main__":
    main()
