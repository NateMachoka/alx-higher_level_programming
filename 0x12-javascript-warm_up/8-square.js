#!/usr/bin/node

const arg = process.argv[2];
const size = parseInt(arg);
let i = 0;

if (!isNaN(size)) {
  for (i; i < size; i++) {
    console.log('X'.repeat(size));
  }
} else {
  console.log('Missing size');
}
