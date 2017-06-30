#!/usr/bin/python3
import sys
import requests


def get_people(j, results):

    for i in results:
        print(i['name'])

    if j['next'] is not None:
        n = requests.get(j['next']).json()
        next_results = n['results']
        get_people(n, next_results)

if __name__ == "__main__":
    params = sys.argv[1]
    r = requests.get('http://swapi.co/api/people/', params={'search': params})
    j = r.json()
    results = j['results']

    print("Number of result: {}".format(j['count']))
    get_people(j, results)
