#!/usr/bin/python3
import sys
import requests


def get_repos():
    repository = sys.argv[1]
    owner = sys.argv[2]

    r = requests.get(
        'https://api.github.com/repos/' + owner + '/' + repository + '/commits'
    )
    json = r.json()

    top10 = json[:10]

    for i in top10:
        print('{}: {}'.format(i['sha'], i['commit']['author']['name']))

if __name__ == "__main__":
    get_repos()
