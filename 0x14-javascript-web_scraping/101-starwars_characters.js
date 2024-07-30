#!/usr/bin/node
// Prints characters in the same order as they appear in 'characters' list in the Star Wars API

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make a GET request to the API URL
request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const movieData = JSON.parse(body);
  const characters = movieData.characters;

  // Function to fetch character data
  const fetchCharacter = (url) => {
    return new Promise((resolve, reject) => {
      request(url, (charError, charResponse, charBody) => {
        if (charError) {
          reject(charError);
        } else {
          resolve(JSON.parse(charBody).name);
        }
      });
    });
  };

  // Array to hold the promises for each character fetch
  const characterPromises = characters.map((characterUrl) => fetchCharacter(characterUrl));

  // Resolve all promises and print the character names in order
  Promise.all(characterPromises)
    .then((names) => {
      names.forEach((name) => {
        console.log(name);
      });
    })
    .catch((err) => {
      console.log(err);
    });
});
