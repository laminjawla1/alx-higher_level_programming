#!/usr/bin/python3
"""
Write a Python script that takes in a letter
and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import sys
import requests


def main():
    """Entry point"""
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data={"q": letter})
    try:
        result = response.json()
        if result:
            print("[{}] {}".format(result.get("id"), result.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
