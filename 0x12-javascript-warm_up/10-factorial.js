#!/usr/bin/node

// Function to compute factorial recursively
function factorial (n) {
  if (isNaN(n) || n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

// Retrieve the first argument and convert it to an integer
const arg = parseInt(process.argv[2]);

console.log(factorial(arg));
