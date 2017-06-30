#!/usr/bin/python3
import requests
import sys


def get_xRequestId():
    url = sys.argv[1]
    r = requests.get(url)
    requestId = r.headers['X-Request-Id']
    print(requestId)

if __name__ == "__main__":
    get_xRequestId()
