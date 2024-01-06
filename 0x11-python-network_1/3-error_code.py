#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the
URL and displays the body of the response (decoded in utf-8).
"""
import sys
import urllib.parse
import urllib.request


def main():
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code), end="")


if __name__ == "__main__":
    main()
