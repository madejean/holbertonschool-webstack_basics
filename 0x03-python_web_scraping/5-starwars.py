#!/usr/bin/python3
import sys
import requests


def search_people():
    r = requests.get('http://swapi.co/api/people/?search=' + sys.argv[1])
    j = r.json()
    results = j['results']
    print("Number of result: {}".format(j['count']))
    for i in results:
        print(i['name'])

if __name__ == "__main__":
    search_people()
