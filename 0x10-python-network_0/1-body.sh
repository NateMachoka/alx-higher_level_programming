#!/bin/bash
# Sends a GET request to the URL, and displays the body of the response
curl -sL -w "%{http_code}" "$1" | tail -n1 | grep -q 200 && curl -sL "$1"
