#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the
URL and displays the body of the response (decoded in utf-8).
"""
import sys
import requests


def main():
    response = requests.get(sys.argv[1])
    code = response.status_code
    if code >= 400:
        print("Error code: {}".format(code))
    else:
        print(response.text)


if __name__ == "__main__":
    main()
