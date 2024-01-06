#!/usr/bin/python3
"""
Write a Python script that takes in a letter
and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import sys
import json
import requests


def main():
    letter = get_letter(sys.argv)
    url = 'http://0.0.0.0:5000/search_user'
    response = requests.post(url, data={'q': letter})
    try:
        result = response.json()
        if not len(result):
            print("No result")
        else:
            print("[{}] {}".format(result.get("id"), result.get("name")))
    except json.JSONDecodeError:
        print("Not a valid JSON")


def get_letter(argv):
    try:
        return argv[1]
    except IndexError:
        return ""


if __name__ == "__main__":
    main()
