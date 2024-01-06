#!/usr/bin/python3
"""
Write a Python script that takes your GitHub
credentials (username and password) and uses
the GitHub API to display your id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


def main():
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/users/{}".format(username)
    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    result = response.json()
    print(result.get("id"))


if __name__ == "__main__":
    main()
