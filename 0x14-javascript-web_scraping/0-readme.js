#!/usr/bin/node

// Reads and prints the content of a file

// Import the 'fs' module to interact with the filesystem
const fs = require('fs');
const filePath = process.argv[2];

// Read the file at the given path using 'utf8' encoding
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
