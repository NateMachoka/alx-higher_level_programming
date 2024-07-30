#!/usr/bin/node
// Display the status code of a GET request.

// Import the 'request' module to make HTTP requests
const request = require('request');
const url = process.argv[2];

// Make a GET request to the specified url
request(url, (error, response) => {
  if (error) {
    console.log(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
