#!/usr/bin/node
// Gets the contents of a webpage and stores it in a file.

// Import modules to make http requests and handle file operations
const request = require('request');
const fs = require('fs');

// Get the URL and file path from command-line arguments
const url = process.argv[2];
const storageFilePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  fs.writeFile(storageFilePath, body, 'utf8', (err) => {
    if (err) {
      console.log(err);
    }
  });
});
