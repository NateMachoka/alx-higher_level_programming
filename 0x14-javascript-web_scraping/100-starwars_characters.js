#!/usr/bin/node

// Import the 'request' module to make HTTP requests
const request = require('request');

// Get the movie ID from the command-line arguments
const movieId = process.argv[2];

// Define the URL for the Star Wars API with the provided movie ID
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make a GET request to the API URL
request(apiUrl, (error, response, body) => {
  // If an error occurs during the request, print the error object
  if (error) {
    console.log(error);
    return;
  }

  // Parse the JSON response body
  const movieData = JSON.parse(body);

  // Extract the list of characters from the movie data
  const characters = movieData.characters;

  // Iterate over each character URL and fetch the character data
  characters.forEach((characterUrl) => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.log(charError);
        return;
      }

      // Parse the JSON response body of the character
      const characterData = JSON.parse(charBody);

      // Print the character name
      console.log(characterData.name);
    });
  });
});
