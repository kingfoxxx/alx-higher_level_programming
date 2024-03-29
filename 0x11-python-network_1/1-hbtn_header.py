#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL
and displays the value of `X-Request-Id`
variable found in the header of the responses.
"""
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as url:
        s = url.getheader('X-Request-Id')
        print("{}".format(s))
