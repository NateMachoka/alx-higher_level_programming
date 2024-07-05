#!/usr/bin/python3
"""
A script that sends a POST request to a specified URL (http://0.0.0.0:5000/search_user)
with a parameter (q) based on user input.
"""
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    try:
        response = requests.post(url, data={'q': q})
        json_response = response.json()

        if json_response:
            print("[{}] {}".format(json_response.get('id'), json_response.get('name')))
        else:
            print("No result")
    
    except ValueError:
        print("Not a valid JSON")
    
    except Exception as e:
        print("Error:", e)
