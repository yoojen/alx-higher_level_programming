#!/usr/bin/python3
"""
fetch url using request package
"""

if __name__ == '__main__':
    import requests

    my_url = "https://intranet.hbtn.io/status"
    html = requests.get(my_url)
    print("Body response:")
    print("\t- type: {}".format(html.text.__class__))
    print("\t- content: {}".format(html.text))
