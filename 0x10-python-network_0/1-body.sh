#!/bin/bash
# Sends a GET request to the URL, and displays the body of the response
curl -sL -w "%{http_code}" "$1" | awk 'END{if ($0 == 200) system("curl -sL "$1)}'
