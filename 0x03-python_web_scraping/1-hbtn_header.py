#!/usr/bin/python3
import requests
import sys


def get_requestId():
    url = sys.argv[1]
    r = requests.get(url)
    requestId = r.headers.get('X-Request-Id')
    print(requestId)

if __name__ == "__main__":
    get_requestId()
