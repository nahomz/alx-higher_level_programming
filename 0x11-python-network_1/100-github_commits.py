#!/usr/bin/python3
'''
gets 10 latest commits of a github repo

usage: ./100-github_commits.py <repo name> <owner>
'''
from sys import argv
import requests

if __name__ == '__main__':
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        argv[1], argv[2])
    res = requests.get(url)
    output = res.json()
    try:
        for i in range(10):
            print('{}: {}'.format(
                output[i].get('sha'),
                output[i].get('commit').get('author').get('name')))
    except IndexError:
        pass
