#!/usr/bin/node

// Visible function from outside that increments a number and calls another function
function addMeMaybe (number, theFunction) {
  number++;
  theFunction(number); // Call the function with the incremented number
}

module.exports = { addMeMaybe };
