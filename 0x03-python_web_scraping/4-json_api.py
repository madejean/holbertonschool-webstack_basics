#!/usr/bin/python3
import sys
import requests


def search_user():
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ''

    r = requests.post('http://54.145.119.185:33424/search_user', data={'q': q})

    try:
        result = r.json()
        if len(result) == 0:
            print("No result")
        else:
            print([result["id"]], result["name"])


    except:
        print("Not a valid JSON")

if __name__ == "__main__":
    search_user()
