#!/usr/bin/node
// Prints the title of a Star Wars movie where the episode number matches a given integer.

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  // If an error occurs, print the error object
  if (error) {
    console.log(error);
  } else {
    // Parse the JSON response body
    const movie = JSON.parse(body);
    // Print the title of the movie
    console.log(movie.title);
  }
});
