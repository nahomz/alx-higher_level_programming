#!/usr/bin/python3
''' takes in a url, sends a request and displays the value of X-Request-id '''
from sys import argv
from urllib.request import urlopen

if __name__ == '__main__':
    url = argv[1]
    with urlopen(url) as res:
        output = res.info().__getitem__('X-Request-Id')
        print(output)
