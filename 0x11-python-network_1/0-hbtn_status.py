#!/usr/bin/python3
''' fetches https://intranet.hbtn.io/status '''
from urllib.request import urlopen

if __name__ == '__main__':
    url = 'https://intranet.hbtn.io/status'
    with urlopen(url) as result:
        output = result.read()
        print('Body response:')
        print('\t- type: {}'.format(type(output)))
        print('\t- content: {}'.format(output))
        print('\t- utf8 content: {}'.format(output.decode('utf-8')))
