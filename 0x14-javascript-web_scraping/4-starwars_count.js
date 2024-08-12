#!/usr/bin/node
// Prints the number of movies where the character “Wedge Antilles” is present.

const request = require('request');
const apiUrl = process.argv[2];
// Define the ID for movie character 'Wedge Antilles'
const AntillesId = 'https://swapi-api.alx-tools.com/api/people/18/';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const data = JSON.parse(body);
  let count = 0;

  // Iterate over each movie in the result
  data.results.forEach(movie => {
    if (movie.characters.includes(AntillesId)) {
      count++;
    }
  });
  console.log(count);
});
