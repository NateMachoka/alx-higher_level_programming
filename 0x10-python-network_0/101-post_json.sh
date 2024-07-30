#!/bin/bash
# Sends a JSON POST request to a URL with the contents of a file as the body
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
