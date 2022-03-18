#!/usr/bin/python3
'''
GET request to url given as param
using requests module
displays value of X-Request-Id
'''
import requests
from sys import argv

if __name__ == '__main__':
    res = requests.get(argv[1])
    print('{}'.format(res.headers.get('x-request-id')))
