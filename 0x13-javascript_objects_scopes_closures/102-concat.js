#!/usr/bin/node

const fs = require('fs');

const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

if (!sourceFile1 || !sourceFile2 || !destinationFile) {
  console.log('Usage: node concat.js <sourceFile1> <sourceFile2> <destinationFile>');
  process.exit(1);
}

const file1Content = fs.readFileSync(sourceFile1, 'utf8');
const file2Content = fs.readFileSync(sourceFile2, 'utf8');

const concatenatedContent = `${file1Content}\n${file2Content}`;

fs.writeFileSync(destinationFile, concatenatedContent);

console.log('Files concatenated successfully.');
