#!/usr/bin/python3
import sys
import requests


def get_user():
    username = sys.argv[1]
    password = sys.argv[2]

    r = requests.get('https://api.github.com/user', auth=(username, password))
    j = r.json()
    try:
        print(j['id'])
    except:
        print('None')

if __name__ == "__main__":
    get_user()
