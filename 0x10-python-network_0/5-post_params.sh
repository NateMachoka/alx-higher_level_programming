#!/bin/bash
# Sends a POST request to a URL with variables and displays the body response
curl -sL -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
