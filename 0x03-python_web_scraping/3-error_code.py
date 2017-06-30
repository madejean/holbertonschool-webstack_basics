#!/usr/bin/python3
import sys
import requests


def get_statusCode():
    url = sys.argv[1]

    r = requests.get(url)

    if (r.status_code >= 400):
        print("Error code:", r.status_code)
    else:
        print(r.text)

if __name__ == "__main__":
    get_statusCode()
