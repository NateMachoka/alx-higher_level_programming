#!/usr/bin/python3
"""
A script that takes in a URL, sends a request to the URL
Displays the body of the response.
If the HTTP status code is greater than or equal to 400, print: Error code:
followed by the value of the HTTP status code
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script_name.py <URL>")
        sys.exit(1)
    
    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes

        # Check if status code is 400 or higher
        if response.status_code >= 400:
            print(f"Error code: {response.status_code}")
        else:
            print(response.text)
    
    except requests.exceptions.HTTPError as e:
        # Error response handling
        print(f"Error code: {e.response.status_code}")
    
    except requests.exceptions.RequestException as e:
        # Connection error handling
        print(f"Error: {e}")
