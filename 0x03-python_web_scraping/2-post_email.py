#!/usr/bin/python3
import sys
import requests


def post_email():
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    r = requests.post(url, data=email)
    print(r.text)

if __name__ == "__main__":
    post_email()
