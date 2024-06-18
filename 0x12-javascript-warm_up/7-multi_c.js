#!/usr/bin/node

const args = process.argv[2];
const x = parseInt(args);
let i = 0;

if (!isNaN(x)) {
  for (i; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
