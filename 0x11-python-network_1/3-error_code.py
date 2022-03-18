#!/usr/bin/python3
'''
takes in a url and sends a GET request
displays the body of the response(utf-8 decoded)

Usage: ./3-error_code.py <url>
'''
from sys import argv
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from urllib.error import HTTPError

if __name__ == '__main__':
    url = argv[1]
    req = Request(url)
    try:
        with urlopen(req) as res:
            print(res.read().decode('utf-8'))
    except HTTPError as e:
        print('Error code: {}'.format(e.code))
