#!/bin/bash
# Sends a GET request to a URL with a custom header and displays the body response
curl -sL -H "X-School-User-Id: 98" "$1"