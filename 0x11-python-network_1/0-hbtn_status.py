#!/usr/bin/python3
"""Fetch url using Request method"""


if __name__ == '__main__':
    from urllib.request import Request, urlopen
    url = Request("https://alx-intranet.hbtn.io/status")
    with urlopen(url) as res:
        html = res.read()
    print("Body response:")
    print("\t-type: {}".format(html.__class__))
    print("\t-content: {}".format(html))
    print("\t-utf8 content: {}".format(html.decode('ascii')))
