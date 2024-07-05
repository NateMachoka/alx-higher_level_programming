#!/usr/bin/python3
"""
A script that takes in a URL, sends a request to the URL
Displays the body of the response.
If the HTTP status code is greater than or equal to 400, print: Error code:
followed by the value of the HTTP status code
"""
import requests
import sys


url = sys.argv[1]

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
    print(response.text)
except requests.exceptions.HTTPError as e:
    print(f"Error code: {e.response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
