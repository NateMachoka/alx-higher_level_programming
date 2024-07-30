#!/usr/bin/node
// Computes the number of tasks completed by user id.

// Import the 'request' module to make HTTP requests
const request = require('request');

// Get the API URL from the command-line arguments
const apiUrl = process.argv[2];

// Make a GET request to the API URL
request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const tasks = JSON.parse(body);
  const userTaskCount = {};

  tasks.forEach(task => {
    if (task.completed) {
      // If the user ID is not yet in the userTaskCount object, initialize it with 0
      if (!userTaskCount[task.userId]) {
        userTaskCount[task.userId] = 0;
      }
      userTaskCount[task.userId]++;
    }
  });

  // Print the user IDs with completed tasks
  console.log(userTaskCount);
});
