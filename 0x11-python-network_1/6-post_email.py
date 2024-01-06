#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
import sys
import requests

def main():
    response = requests.post(sys.argv[1], data={"email": sys.argv[2]})
    print(response.content)

if __name__ == "__main__":
    main()
