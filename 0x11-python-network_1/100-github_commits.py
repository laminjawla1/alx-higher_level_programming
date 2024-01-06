#!/usr/bin/python3
"""
The Holberton School staff evaluates candidates
applying for a back-end position with multiple
technical challenges, like this one:
"""
import sys
import requests


def main():
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(repo, owner)
    response = requests.get(url)
    result = response.json()
    for commit in result[:10]:
        print(
            "{}: {}".format(
                commit.get("sha"),
                commit.get("commit").get("author").get("name")
            )
        )


if __name__ == "__main__":
    main()
