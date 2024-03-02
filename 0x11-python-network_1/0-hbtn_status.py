#!/usr/bin/python3
"""
fetch https://intranet.hbtn.io/status; display response
"""

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        html = res.read()
        print('Body res:')
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
