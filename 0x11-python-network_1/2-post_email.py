#!/usr/bin/python3
'''
takes in a url and email, sends a POST request
displays the body of the response(utf-8 decoded)

Usage: ./2-post_email.py <url> <email>
'''
from sys import argv
from urllib.request import urlopen, Request
from urllib.parse import urlencode

if __name__ == '__main__':
    url = argv[1]
    email = {'email': argv[2]}
    data = urlencode(email).encode('ascii')
    req = Request(url, data)
    with urlopen(req) as res:
        print(res.read().decode('utf-8'))
