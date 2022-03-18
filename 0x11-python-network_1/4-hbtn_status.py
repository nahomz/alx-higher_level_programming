#!/usr/bin/python3
''' GET request to https://intranet.hbtn.io/status using requests module '''
import requests

if __name__ == '__main__':
    res = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(res.text)))
    print('\t- content: {}'.format(res.text))
