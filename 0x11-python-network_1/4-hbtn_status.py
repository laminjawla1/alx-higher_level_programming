#!/usr/bin/python3
"""
Implemments a python script to get the status of a route
"""

import requests


def main():
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    body = response.content.decode("utf-8")

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))


if __name__ == "__main__":
    main()
