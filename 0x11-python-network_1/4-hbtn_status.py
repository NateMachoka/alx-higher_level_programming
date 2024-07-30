#!/usr/bin/python3
"""
A script that fetches https://alx-intranet.hbtn.io/status
using the package requests and prints the response body
"""
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    content = response.text

    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))