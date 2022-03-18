#!/usr/bin/python3
'''
takes in url and email address
sends POST request to url
displays body of the response

Usage: ./6-post_email.py <url> <email>
'''
from sys import argv
import requests

if __name__ == '__main__':
    url = argv[1]
    email = {'email': argv[2]}
    res = requests.post(url, data=email)
    print(res.text)
