#!/usr/bin/node

// Retrieve command-line arguments and convert them to integers
const args = process.argv.slice(2).map(Number);

// Function to find the second largest number
function secondBiggest (nums) {
  if (nums.length < 2) {
    return 0;
  }

  // Sort the numbers in descending order
  nums.sort((a, b) => b - a);

  // Return the second largest number
  return nums[1];
}

// Print the result
console.log(secondBiggest(args));
