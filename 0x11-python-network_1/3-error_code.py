#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the
body of the response (decoded in utf-8)
"""
import urllib.request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            print(response.read().decode())
    except urllib.error.URLError as err:
        print("Error code: {}".format(err.code))
