#!/bin/bash
# Retrieves and displays all HTTP methods accepted by a server for a URL
curl -sI "$1" | grep -i '^Allow:' | cut -d ' ' -f 2-
